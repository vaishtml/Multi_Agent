import re
from tools import CalculatorTool, WeatherTool, StringTool, UnitConversionTool

class Agent:
    def __init__(self, name):
        self.name = name

    def handle_query(self, query):
        raise NotImplementedError

class CalculatorAgent(Agent):
    def __init__(self):
        super().__init__("CalculatorAgent")
        self.tool = CalculatorTool()

    def handle_query(self, query):
        lower_query = query.lower()

        # Check for addition (e.g., "add 5 and 7", "5+7")
        if any(word in lower_query for word in ["add", "plus", "+"]):
            numbers = re.findall(r'\d+', lower_query)
            if len(numbers) >= 2:
                num1, num2 = int(numbers[0]), int(numbers[1])
                return self.tool.add(num1, num2)

        # Check for multiplication (e.g., "multiply 3 by 4", "3*4")
        elif any(word in lower_query for word in ["multiply", "times", "*"]):
            numbers = re.findall(r'\d+', lower_query)
            if len(numbers) >= 2:
                num1, num2 = int(numbers[0]), int(numbers[1])
                return self.tool.multiply(num1, num2)
            
        # Check for subtraction (e.g., "subtract 10 from 5", "10-5")
        elif any(word in lower_query for word in ["subtract", "minus", "-"]):
            numbers = re.findall(r'\d+', lower_query)
            if len(numbers) >= 2:
                num1, num2 = int(numbers[0]), int(numbers[1])
                return self.tool.subtract(num1, num2)
        
        # Check for division (e.g., "divide 8 by 2", "8/2")
        elif any(word in lower_query for word in ["divide", "/", "by"]):
            numbers = re.findall(r'\d+', lower_query)
            if len(numbers) >= 2:
                num1, num2 = int(numbers[0]), int(numbers[1])
                return self.tool.divide(num1, num2)
        return None

class WeatherAgent(Agent):
    def __init__(self):
        super().__init__("WeatherAgent")
        self.tool = WeatherTool()

    def handle_query(self, query):
        if "weather" in query.lower():
            # Use regex to find either "weather in" or "weather of" followed by a city name
            match = re.search(r"weather (?:in|of) (.+)", query, re.IGNORECASE)
            if match:
                city = match.group(1).strip()
                return self.tool.get_weather(city)
        return None

class StringAgent(Agent):
    def __init__(self):
        super().__init__("StringAgent")
        self.tool = StringTool()

    def handle_query(self, query):
        if "reverse" in query.lower():
            # New regex to find text inside double quotes
            match = re.search(r'"(.+)"', query)
            if match:
                s = match.group(1).strip()
                return self.tool.reverse_string(s)
            
            # Fallback to the old logic if no quotes are found
            match = re.search(r"reverse (.+)", query, re.IGNORECASE)
            if match:
                s = match.group(1).strip()
                return self.tool.reverse_string(s)
                
        elif "uppercase" in query.lower():
            # Reusing the new regex for consistency
            match = re.search(r'"(.+)"', query)
            if match:
                s = match.group(1).strip()
                return self.tool.uppercase_string(s)

            match = re.search(r"uppercase (.+)", query, re.IGNORECASE)
            if match:
                s = match.group(1).strip()
                return self.tool.uppercase_string(s)
            
        elif "lowercase" in query.lower():
            match = re.search(r'"(.+)"', query)
            if match:
                s = match.group(1).strip()
                return self.tool.lowercase_string(s)

            match = re.search(r"lowercase (.+)", query, re.IGNORECASE)
            if match:
                s = match.group(1).strip()
                return self.tool.lowercase_string(s)

        elif "palindrome" in query.lower():
            # New regex to handle questions like "is apple a palindrome?"
            match = re.search(r"is\s+(.+)\s+a\s+palindrome\??", query)
            if not match:
                # Fallback for simple queries like "palindrome apple"
                match = re.search(r"palindrome\s+(.+)", query)

            if match:
                s = match.group(1).strip()
                is_palindrome = self.tool.palindrome_check(s)
                if is_palindrome:
                    return f'"{s}" is a palindrome.'
                else:
                    return f'"{s}" is not a palindrome.'

        elif "count vowels" in query.lower():
        # New regex to handle questions like "how many vowels are in 'apple'?"
            match = re.search(r'"(.+)"', query)
            if not match:
            # Fallback for simple queries like "count vowels in apple"
                match = re.search(r"count vowels in (.+)", query, re.IGNORECASE)
            
            if match:
                s = match.group(1).strip()
                count = self.tool.count_vowels(s)
                return f'The string "{s}" has {count} vowels.'

        elif "count consonants" in query.lower():
        # New regex to handle questions like "how many consonants are in 'apple'?"
            match = re.search(r'"(.+)"', query)
            if not match:
            # Fallback for simple queries like "count consonants in apple"
                match = re.search(r"count consonants in (.+)", query, re.IGNORECASE)

            if match:
                s = match.group(1).strip()
                count = self.tool.count_consonants(s)
                return f'The string "{s}" has {count} consonants.'

        return None
    

class UnitConversionAgent(Agent):
    def __init__(self):
        super().__init__("UnitConversionAgent")
        self.tool = UnitConversionTool()

    def handle_query(self, query):
        lower_query = query.lower()

        # Length conversions
        if "cm to m" in lower_query:
            match = re.search(r"(\d+)\s*cm to m", lower_query)
            if match:
                amount = int(match.group(1))
                return f"{amount} cm is {self.tool.convert_cm_to_m(amount)} m."
        elif "m to cm" in lower_query:
            match = re.search(r"(\d+)\s*m to cm", lower_query)
            if match:
                amount = int(match.group(1))
                return f"{amount} m is {self.tool.convert_m_to_cm(amount)} cm."
        elif "km to m" in lower_query:
            match = re.search(r"(\d+)\s*km to m", lower_query)
            if match:
                amount = int(match.group(1))
                return f"{amount} km is {self.tool.convert_km_to_m(amount)} m."
            
        elif "m to km" in lower_query:
            match = re.search(r"(\d+)\s*m to km", lower_query)
            if match:
                amount = int(match.group(1))
                return f"{amount} m is {amount / 1000} km."
        


        # Weight conversions
        elif "kg to g" in lower_query:
            match = re.search(r"(\d+)\s*kg to g", lower_query)
            if match:
                amount = int(match.group(1))
                return f"{amount} kg is {self.tool.convert_kg_to_g(amount)} g."
        elif "g to kg" in lower_query:
            match = re.search(r"(\d+)\s*g to kg", lower_query)
            if match:
                amount = int(match.group(1))
                return f"{amount} g is {self.tool.convert_g_to_kg(amount)} kg."
        
        return None

class MasterAgent(Agent):
    def __init__(self):
        super().__init__("MasterAgent")
        self.agents = [
            CalculatorAgent(),
            WeatherAgent(),
            StringAgent(),
            UnitConversionAgent()
        ]

    def route_query(self, query):
        for agent in self.agents:
            response = agent.handle_query(query)
            if response is not None:
                return response
        
        # Fallback for unrecognized queries
        return "I'm sorry, I can only help with calculations, weather, and string manipulations."