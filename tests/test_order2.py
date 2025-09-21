import allure
from data import TestMessages, URL, CourierService, color_selection
from helpers import Order
import pytest

# Класс с тестами для заказа с порядковым номером V1
class TestOrderCreationV1:
    @allure.title('Test_Create_Order_With_Valid_Data_And_Color_Selection_001')
    @allure.description('Отправляем POST-запрос на создание заказа с валидными данными и указанием цвета, проверяем код и тело ответа')
    @allure.link(URL, name='Учебный сервис «Яндекс.Самокат»')
    
    @pytest.mark.parametrize('color', color_selection)
    def test_create_order_with_valid_data_001(self, random_order, color):
        random_order["color"] = color
        response = Order.create_order(random_order)
        
        # Проверки
        assert response.status_code == TestMessages.ORDER_SUCCESSFUL_CREATION_WITH_VALID_VALUES["code"]
        assert TestMessages.ORDER_SUCCESSFUL_CREATION_WITH_VALID_VALUES["message"] in response.json()

# Класс с тестами для проверки списка заказов с порядковым номером V1
class TestOrdersListV1:
    @allure.title('Test_Get_Orders_List_Successfully_002')
    @allure.description('Проверка получения списка заказов: код ответа 200 и наличие ключа «orders» в ответе')
    @allure.link(URL, name='Учебный сервис «Яндекс.Самокат»')
    
    def test_get_orders_list_successfully_002(self):
        response = Order.view_orders()
        
        # Проверки
        assert response.status_code == TestMessages.ORDER_GET_LIST_OF_ORDERS["code"]
        assert TestMessages.ORDER_GET_LIST_OF_ORDERS["message"] in response.json()