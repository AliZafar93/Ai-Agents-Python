class InvoiceAgent:
    def __init__(self, invoices):
        self.invoices = invoices

    def send_reminders(self):
        for invoice in self.invoices:
            if not invoice['paid']:
                print(f"Sending reminder for invoice {invoice['id']}")

    def update_payments(self, payment):
        for invoice in self.invoices:
            if invoice['id'] == payment['id']:
                invoice['paid'] = True
                print(f"Payment updated for invoice {invoice['id']}")

# Sample usage
invoices = [{"id": 1, "paid": False}, {"id": 2, "paid": False}]
agent = InvoiceAgent(invoices)
agent.send_reminders()
agent.update_payments({"id": 1})


# class ShoppingAssitant:
#     def __init__(self, budget, preferences, discounts):
#         self.budget = budget
#         self.preferences = preferences
#         self.discounts = discounts

#     def maximize_satisfaction(self, items):
#         total_cost = 0
#         selected_items = []
#         for item, (cost, preference) in items.items():
#             if total_cost + cost <= self.budget:
#                 total_cost += cost
#                 selected_items.append(item)
#         return selected_items

# agent = ShoppingAssitant(100, {"Laptop": 5, "Smartphone": 3}, {"Laptop": 10, "Smartphone": 5})
# items = {"Laptop": (50, 5), "Smartphone": (30, 3)}
# print(agent.maximize_satisfaction(items))

# class SchedulingAgent:
#     def __init__(self, skills, availability, preferences):
#         self.skills = skills
#         self.availability = availability
#         self.preferences = preferences

#     def choose_shift(self, shifts):
#         best_score = -1
#         for shift in shifts:
#             score = self.skills.get(shift, 0) + self.availability.get(shift, 0) + self.preferences.get(shift, 0)
#             if score > best_score:
#                 best_score = score
#                 best_shift = shift
#         return best_shift

# agent = SchedulingAgent({"morning": 5, "evening": 3}, {"morning": 2, "evening": 4}, {"morning": 1, "evening": 5})
# print(agent.choose_shift(["morning", "evening"]))


# def UtilityAgent(decisions):
#     max_utility = 0
#     for action, utility in decisions.items():
#         if utility > max_utility:
#             max_utility = utility
#             best_action = action
#     return best_action

# decisions = {"buy_food": 5, "buy_clothes": 1, "buy_electronics": 2}
# print(UtilityAgent(decisions))


# class CompleteTasks:
#     def __init__(self, tasks):
#         self.tasks = tasks
#         self.current_task = 0

#     def complete_task(self):
#         while self.current_task < len(self.tasks):
#             print(f"Completing task: {self.tasks[self.current_task]}")
#             self.current_task += 1    
#         print("All tasks completed.")
            

# agent = CompleteTasks(["Doctor Appointment", "Technical Writing Quiz", "AI Assignment #2"])
# agent.complete_task()


# def reative_agent(environment):
#     if environment == "obstacle_left":
#         return "Move towards right"
#     elif environment == "obstacle_right":
#         return "Move towards left"
#     return "Move forward"

# print(reative_agent("obstacle_right"))
# print(reative_agent("obstacle_left"))
# print(reative_agent("obstacle_at_both_sides"))

# class SmartThermostat:
#     def __init__(self, temp):
#         self.current_temp = temp
#         self.adjustments = []

#     def adjust(self, desired_temp):
#         change = desired_temp - self.current_temp
#         self.adjustments.append(change)
#         self.current_temp += change // 2
#         return f"Adjusted temperature to {self.current_temp} degree centigrade"
    
# thermo = SmartThermostat(22)
# print(thermo.adjust(26))
# print(thermo.adjust(26))

# class LearningChatbot:
#     def __init__(self):
#         self.knowledge = {}

#     def learn(self, question, answer):
#         self.knowledge[question] = answer

#     def respond(self, question):
#         return self.knowledge.get(question, "I don't know. Teach me!")
    
# chatbot = LearningChatbot()
# chatbot.learn("How are you?", "I'm good, thanks!")
# print(chatbot.respond("How are you?"))
# print(chatbot.respond("What is AI?"))


# def drone_navigation(weather):
#     if weather == "Clear":
#         return "Proceed with flight"
#     return "Delay flight"

# print(drone_navigation("Rainy"))


# def save_energy(usage):
#     if usage > 100:
#         return "Turn off non-essential devices"
#     return "Energy usage is normal"

# print(save_energy(85))


# def recommend_product(user_preference):
#     if user_preference == "Electronics":
#         return "Recommend: Laptop"
#     return "Recommend: Clothing"

# print(recommend_product("Electronics"))


# def choose_move(opponent_move):
#     if opponent_move == "Attack":
#         return "Defend"
#     return "Counter Attack"

# print(choose_move("Attack"))

# def solve_maze(current_position, goal_position):
#     if current_position == goal_position:
#         return "Reached goal"
#     return "Move towards goal"

# print(solve_maze((1,2),(3,3)))

# def drive(destination):
#     if destination == "Home":
#         return "taking shortest route to Home"
#     elif destination == "Office":
#         return "Taking fastest route to Office"
#     return "Destination unknown"

# print(drive("Office"))


# class Elevator:
#     def __init__(self):
#         self.current_floor = 1

#     def move_to(self, target_floor):
#         if target_floor > self.current_floor:
#             return "Going up"
#         elif target_floor < self.current_floor:
#             return "Going down"
#         return "Already on the floor"
    
# elevator = Elevator()
# print(elevator.move_to(5))


# class Thermostat:
#     def __init__(self):
#         self.current_temp = 22

#     def adjust_temperature(self, desired_temp):
#         if self.current_temp > desired_temp:
#             return "Cooling down..."
#         elif self.current_temp < desired_temp:
#             return "Heating up..."
#         return "Temperature is perfect"
    
# thermo = Thermostat()
# print(thermo.adjust_temperature(18))


# class VacuumCleaner:
#     def __init__(self):
#         self.room_state = {"Living Room": "dirty", "Kitchen": "clean"}

#     def clean(self, room):
#         if self.room_state[room] == "dirty":
#             self.room_state[room] = "clean"
#             return f"Cleaning {room}"
#         return f"{room} is already clean"

# vacuum = VacuumCleaner()
# print(vacuum.clean("Living Room"))
# print(vacuum.clean("Kitchen"))

# def spam_filter(email_text):
#     spam_keywords = ["lottery","prize","winner"]
#     for word in spam_keywords:
#         if word in email_text.lower():
#             return "Spam Email"
#     return "Not Spam"

# print(spam_filter("You won a prize!"))



# def traffic_light(color):
#     if color == "Red":
#         return "Stop"
#     elif color == "Yellow":
#         return "Slow Down"
#     elif color == "Green":
#         return "Go"
#     else:
#         return "Invalid Color"
    
# print(traffic_light("Yellow"))



# def heater_control(temperature):
#     if temperature < 20:
#         return "Turn ON heater"
#     else:
#         return "Turn OFF heater"
    
# print(heater_control(2))