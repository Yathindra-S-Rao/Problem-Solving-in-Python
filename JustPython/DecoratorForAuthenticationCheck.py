def requires_login(func):
    def wrapper(*args, **kwargs):
        if not kwargs.get("logged_in"):
            print("Access Denied")
            return 
        func(*args, **kwargs)
    return wrapper

@requires_login
def render_dashboard(*args, **kwargs):
    print("Dashboard Rendered") 
    
render_dashboard(logged_in=True)
render_dashboard(logged_in=False) 