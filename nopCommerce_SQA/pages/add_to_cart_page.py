from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class AddCartPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    quantity="//input[@id='product_enteredQuantity_20']"
    add_to_cart="//button[@id='add-to-cart-button-20']"
    shopping_cart="//a[normalize-space()='shopping cart']"
    def getQuantity(self):
        return self.wait_elements_clickable(By.XPATH, self.quantity)
    def getAddToCart(self):
        return self.wait_elements_clickable(By.XPATH, self.add_to_cart)
    def getShoppingCart(self):
        return self.wait_elements_clickable(By.XPATH, self.shopping_cart)
    def enterQuantity(self,quantity):
        self.getQuantity().clear()
        self.getQuantity().send_keys(quantity)
    def clickAddToCart(self):
        self.getAddToCart().click()
    def clickShoppingCart(self):
        self.getShoppingCart().click()
    def addToCart(self,quantity):
        self.enterQuantity(quantity)
        self.clickAddToCart()
        self.clickShoppingCart()


