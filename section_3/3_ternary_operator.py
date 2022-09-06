# Ternary Operator

# condition_if_true if condtion else condition_if_else
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)

# Short circuting
 
# here Not Matter What second conditio is if the first condition is true then the if block will be run.
Is_friend = True
is_user = True

if Is_friend or is_user :
    print("Best Friend Forever")