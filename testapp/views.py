from django.shortcuts import render

# Create your business LOGIC / views here.

# Page Count View
def page_count_view(request):
    print('='*45)
    print(request.COOKIES)  # For Checking Purpose
    print('='*55)

    count = request.session.get('count', 0)  # Fetch Data from Session, If not found display 0
    count += 1  # Store count after updation

    request.session['count'] = count  # Assigining the updated count data
    request.session.set_expiry(10)  # After the particular time Session Expire

    return render(request, 'testapp/page_count.html', {'count':count})
