#write a Python program to check whether a product launch can proceed when development is complete, testing is passed, and approval is received.
development_complete = True
testing_passed = True
approval_received = True

if development_complete and testing_passed and approval_received:
    print("Product launch can proceed.")
else:
    print("Product launch cannot proceed.")
