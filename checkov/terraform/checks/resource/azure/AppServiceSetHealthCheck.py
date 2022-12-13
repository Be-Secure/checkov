from checkov.common.models.enums import CheckCategories
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck
from checkov.common.models.consts import ANY_VALUE


class AppServiceSetHealthCheck(BaseResourceValueCheck):
    def __init__(self):
        # "Azure App Service monitors a specific path for each web app instance to determine health status.
        # The monitored path should implement functional checks to determine if the app is performing correctly.
        # The checks should include dependencies including those that may not be regularly called.
        # Regular checks of the monitored path allow Azure App Service to route traffic based on availability."
        name = "Ensure that App Service sets Web Probe"
        id = "CKV_AZURE_213"
        supported_resources = ('azurerm_app_service', 'azurerm_linux_web_app', 'azurerm_windows_web_app')
        categories = (CheckCategories.IAM,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self):
        return 'site_config/[0]/health_check_path'

    def get_expected_values(self):
        return ANY_VALUE


check = AppServiceSetHealthCheck()
