*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  jaakko  jaakko123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  paavo  paavo321
    Output Should Contain  User with username paavo already exists

Register With Invalid Username And Valid Password
    Input Credentials  paavo+  paavo321
    Output Should Contain  Username can't contain special characters

Register With Too Short Username And Valid Password
    Input Credentials  ab  paavo321
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input Credentials  jaakko  123
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  jaakko  jaakkojaakko
    Output Should Contain  Password has to contain at least one special character

*** Keywords ***
Input New Command And Create User
    Create User  paavo  paavo123
    Input New Command