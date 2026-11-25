from django.test import TestCase


class AgeGateTests(TestCase):
    def test_unverified_visitors_are_redirected_to_age_gate(self):
        response = self.client.get("/about/")

        self.assertRedirects(response, "/")
        self.assertContains(self.client.get("/"), "Age verification")

    def test_underage_submission_does_not_unlock_pages(self):
        response = self.client.post("/", {"age": "17"})

        self.assertContains(response, "You must be 18 or older")
        self.assertContains(response, "<script>alert(")
        self.assertNotIn("age_verified", self.client.session)
        self.assertRedirects(self.client.get("/contact/"), "/")

    def test_age_18_unlocks_site_pages(self):
        response = self.client.post("/", {"age": "18"}, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'alert("Welcome! Age verified successfully.");')
        self.assertNotContains(self.client.get("/"), 'alert("Welcome! Age verified successfully.");')
        self.assertEqual(self.client.get("/about/").status_code, 200)
        self.assertEqual(self.client.get("/contact/").status_code, 200)
