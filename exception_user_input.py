
class NotAllowPercentage(Exception):
    pass

def calculate_percentage()->float:
    try:
        num = int(input("Enter your number: "))
        percentage = int(input("Enter your percentage(Do not allow 1-5%): "))
        # Do not allow 1-5%
        if percentage<=5:
            raise NotAllowPercentage("Do not allow 1-5 %")
        return (percentage * 100) / num
    except (ValueError, NotAllowPercentage) as exp:
        print(exp)
        calculate_percentage()

result = calculate_percentage()
print(result)
