from django.shortcuts import render

def index(request):
    result = None  # Initialize result to avoid UnboundLocalError
    
    if request.method == "POST":
        num1 = request.POST.get('first_number')
        num2 = request.POST.get('second_number')
        oper = request.POST.get('operation')

        try:
            num1 = float(num1)
            num2 = float(num2)
            if oper == 'add':
                result = num1 + num2
            elif oper == 'subtract':
                result = num1 - num2
            elif oper == 'multiply':
                result = num1 * num2
            elif oper == 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Not divisible by 0"
            else:
                result = "Invalid operation"
        except (ValueError, TypeError):
            result = "Invalid input"

    return render(request, 'index.html', {'result': result})
