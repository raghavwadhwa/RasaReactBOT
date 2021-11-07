# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3

class ActionSpentMoney(Action):
    
    def name(self) -> Text:
        return "action_spent_money"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn = sqlite3.connect('myntra.db')
        email=tracker.sender_id
        query=str(str(email)+"@gmail.com")
        query1='"'+query+'"'
        h=None
        cursor = conn.execute("SELECT spending_done from User WHERE email="+query1)
        for i in cursor:
            val=i[0]
            dispatcher.utter_message(text="You have spent Rs."+str(val)+" till now.")
            return ""

#done
class ActionLastOrder(Action):
    
    def name(self) -> Text:
        return "action_last_order"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn = sqlite3.connect('myntra.db')
        email=tracker.sender_id
        query=str(str(email)+"@gmail.com")
        query1='"'+query+'"'
        print(query)
        order_id = conn.execute("SELECT order_id from mapping_orders_user WHERE user_email="+query1) # extracting id from mapping table
        for j in order_id:
            val=j[0]
            print(val)
            cursor = conn.execute("SELECT name from orders WHERE order_id=" + str(val)) # getting name of last bought product
            for i in cursor:
                val=i[0]
                dispatcher.utter_message(text=val)
                return []
        
#done
class ActionShippingOrders(Action):
    
    def name(self) -> Text:
        return "action_shipping_address"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn = sqlite3.connect('myntra.db')
        email=tracker.sender_id
        query=str(str(email)+"@gmail.com")
        query1='"'+query+'"'
        order_id = conn.execute("SELECT order_id from mapping_orders_user WHERE user_email="+query1 ) # extracting id from mapping table
        for j in order_id:
            val=j[0]
            print(val)
            cursor = conn.execute("SELECT shipping_address from orders WHERE order_id=" + str(val)) # getting name of last bought product
            for i in cursor:
                val=i[0]
                dispatcher.utter_message(text=val)
                return ""
        
#done
class ActionTrackOrder(Action):
    def name(self) -> Text:
        return "action_track_order"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn = sqlite3.connect('myntra.db')
        email=tracker.sender_id
        query=str(str(email)+"@gmail.com")
        query1='"'+query+'"'
        order_id = conn.execute("SELECT order_id from mapping_orders_user WHERE user_email="+query1 ) # extracting id from mapping table
        for j in order_id:
            val=j[0]
            print(val)
            cursor = conn.execute("SELECT last_checkpoint_of_ordered_product from orders WHERE order_id=" + str(val)) # getting name of last bought product
            for i in cursor:
                val=i[0]
                dispatcher.utter_message(text="Your order is presently at "+val)
                return ""

        
            
#parasmadan555
class ActionOrderHistory(Action):
    
    def name(self) -> Text:
        return "action_previous_orders"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn = sqlite3.connect('myntra.db')
        email=tracker.sender_id
        query=str(str(email)+"@gmail.com")
        query1='"'+query+'"'
        order_ids = conn.execute("SELECT order_id from mapping_orders_user WHERE user_email="+query1 ) 
        l=""
        #order_ids = conn.execute("SELECT order_id from mapping_orders_user WHERE email="+str(email) ) # extracting id from mapping table
        for j in order_ids:
            val=j[0]
            print(val)
            cursor = conn.execute("SELECT name from orders WHERE order_id=" + str(val)) # getting name of last bought product
            for i in cursor:
                val=i[0]
                l += val
                l += ", "
            l = l[:-2]
        dispatcher.utter_message(text=str(l))
        return ""

# done
class ActionProductCategory(Action):
    def name(self) -> Text:
        return "action_products_category"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn = sqlite3.connect('myntra.db')
        cursor = conn.execute("SELECT category_name from product_categories") # getting name of last bought product
        l = ""
        for i in cursor:
            val=i[0]
            l += val
            l += ", "
        l = l[:-2]
        print(l)
        dispatcher.utter_message(text=str(l))
        return ""

class ActionProductShoes(Action):
    
    def name(self) -> Text:
        return "action_product_shoes"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn = sqlite3.connect('myntra.db')
        cursor = conn.execute("SELECT name from product_shoes") # getting name of last bought product
        l=""
        for i in cursor:
            val=i[0]
            l += val
            l += ', '
        l = l[:-2]
        dispatcher.utter_message(text=str(l))
        return ""
class ActionProductGadgets(Action):
    
    def name(self) -> Text:
        return "action_product_gadgets"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn = sqlite3.connect('myntra.db')
        cursor = conn.execute("SELECT name from product_gadgets") # getting name of last bought product
        l=""
        for i in cursor:
            val=i[0]
            l += val
            l += ", "
        l = l[:-2]
        dispatcher.utter_message(text=str(l))
        return ""

class ActionProductClothing(Action):
    def name(self) -> Text:
        return "action_product_clothing"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn = sqlite3.connect('myntra.db')
        cursor = conn.execute("SELECT name from product_clothing") # getting name of last bought product
        l=""
        for i in cursor:
            val=i[0]
            l += val
            l += ', '
        l = l[:-2]
        dispatcher.utter_message(text='We sell the following in clothing section '+str(l))
        return ""

# cart 
# parasmadan555
class ActionCart(Action):
    
    def name(self) -> Text:
        return "action_cart"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn = sqlite3.connect('myntra.db')
        email=tracker.sender_id
        query=str(str(email)+"@gmail.com")
        query1='"'+query+'"'
        #order_ids = conn.execute("SELECT order_id from mapping_orders_user WHERE user_email="+query1 ) 
        product_ids = conn.execute("SELECT product_id from mapping_cart_user WHERE user_email="+query1 ) # extracting id from mapping table
        l = ""
        for i in product_ids:
            product_id=i[0]
            cursor = conn.execute("SELECT category_name from product_categories WHERE category_id=" + str(product_id)) 
            for j in cursor:
                l += j[0]
                l += ", "
        l = l[:-2]
        print(l)
        dispatcher.utter_message(text=str(l))
        return ""




