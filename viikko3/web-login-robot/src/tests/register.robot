*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  paavo
    Set Password  paavo123
    Set Password Confirmation  paavo123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  pa
    Set Password  paavo123
    Set Password Confirmation  paavo123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  paavo
    Set Password  paavo1
    Set Password Confirmation  paavo1
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  paavo
    Set Password  paavo123
    Set Password Confirmation  paavo124
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation don't match

Login After Successful Registration
    Set Username  paavo
    Set Password  paavo123
    Set Password Confirmation  paavo123
    Submit Credentials
    Register Should Succeed
    Go to Login Page
    Login Page Should Be Open
    Set Username  paavo
    Set Password  paavo123
    Submit Login
    Login Should Succeed

Login After Failed Registration
    Set Username  pa
    Set Password  paavo123
    Set Password Confirmation  paavo123
    Submit Credentials
    Register Should Fail With Message  Username too short
    Go To Login Page
    Login Page Should Be Open
    Set Username  pa
    Set Password  paavo123
    Submit Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open
    
Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Login
    Click Button  Login

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}