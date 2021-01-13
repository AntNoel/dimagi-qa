from Pages.homePage import HomePage
from TestBase.environmentSetupPage import EnvironmentSetup


class MenuVisibilityTests(EnvironmentSetup):

    def test_01_reports_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        visible.reports_menu()
        assert "My Saved Reports : Project Reports :: - CommCare HQ" in driver.title

    def test_02_dashboard_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        visible.dashboard_menu()
        assert "CommCare HQ" in driver.title

    def test_03_application_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        visible.applications_menu()
        assert "Releases - Untitled Application - CommCare HQ" in driver.title

    def test_04_user_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        visible.users_menu()
        assert "Mobile Workers : Users :: - CommCare HQ" in driver.title

    def test_05_data_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        visible.data_menu()
        assert "Export Form Data : Data :: - CommCare HQ" in driver.title

    def test_06_web_apps_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        visible.web_apps_menu()
        assert "Web Apps - CommCare HQ" in driver.title

    def test_07_messaging_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        visible.messaging_menu()
        assert "Dashboard : Messaging :: - CommCare HQ" in driver.title

    # def test_08_admin_menu_visibility(self):
    #     driver = self.driver
    #     visible = HomePage(driver)
    #     visible.admin_menu()
    #     assert "User List - CommCare HQ" in driver.title
