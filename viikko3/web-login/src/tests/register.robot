*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  testA
    Set Password  abcd1234
    Set Password Confirmation  abcd1234
    Submit Registration
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  abcd1234
    Set Password Confirmation  abcd1234
    Submit Registration
    Register Should Fail With Message  Username must have only letters and at least 3 characters

Register With Valid Username And Invalid Password
    Set Username  testB
    Set Password  abcdefg
    Set Password Confirmation  abcdefg
    Submit Registration
    Register Should Fail With Message  Password must have a non letter character and at least 8 characters

Register With Nonmatching Password And Password Confirmation
    Set Username  testC
    Set Password  abcd1234
    Set Password Confirmation  none
    Submit Registration
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Set Username  testD
    Set Password  abcd1234
    Set Password Confirmation  abcd1234
    Submit Registration
    Register Should Succeed
    Go To Main Page
    Click Button  Logout
    Set Username  testD
    Set Password  abcd1234
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  b
    Set Password  abcd1234
    Set Password Confirmation  abcd1234
    Submit Registration
    Register Should Fail With Message  Username must have only letters and at least 3 characters
    Go To Login Page
    Set Username  b
    Set Password  abcd1234
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Registration
    Click Button  Register

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}