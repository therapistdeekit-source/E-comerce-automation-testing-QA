from playwright.sync_api import Page, expect


class SignupPage:
    def __init__(self, page: Page):
        self.page = page

    def register(
        self,
        *,
        username: str,
        email: str,
        password: str,
        birth_day: str,
        birth_month: str,
        birth_year: str,
        first_name: str,
        last_name: str,
        company: str,
        address: str,
        address_2: str,
        country: str,
        state: str,
        city: str,
        zipcode: str,
        mobile_number: str,
    ) -> None:
        self.page.goto("https://automationexercise.com/signup")

        signup_form = self.page.locator("form").filter(has_text="Signup")
        signup_form.get_by_placeholder("Name").fill(username)
        signup_form.get_by_placeholder("Email Address").fill(email)
        signup_form.get_by_role("button", name="Signup").click()

        self.page.get_by_role("radio", name="Mr.").check()
        self.page.get_by_role("textbox", name="Password *").fill(password)
        self.page.locator("#days").select_option(birth_day)
        self.page.locator("#months").select_option(birth_month)
        self.page.locator("#years").select_option(birth_year)

        fields = {
            "First name *": first_name,
            "Last name *": last_name,
            "Company": company,
            "Address * (Street address, P.": address,
            "Address 2": address_2,
            "State *": state,
            "City * Zipcode *": city,
            "Mobile Number *": mobile_number,
        }
        for label, value in fields.items():
            self.page.get_by_role(
                "textbox", name=label, exact=(label == "Company")
            ).fill(value)

        self.page.get_by_label("Country *").select_option(country)
        self.page.locator("#zipcode").fill(zipcode)
        self.page.get_by_role("button", name="Create Account").click()
        expect(
            self.page.get_by_text(
                "Account Created! Congratulations! Your new account has been successfully"
            )
        ).to_be_visible()

    def enter_login_email(self, email: str) -> None:
        login_form = self.page.locator("form").filter(has_text="Login")
        login_form.get_by_placeholder("Email Address").fill(email)

    def enter_password(self, password: str) -> None:
        self.page.get_by_role("textbox", name="Password").fill(password)

    def click_login_button(self) -> None:
        login_form = self.page.locator("form").filter(has_text="Login")
        login_form.get_by_role("button", name="Login").click()
