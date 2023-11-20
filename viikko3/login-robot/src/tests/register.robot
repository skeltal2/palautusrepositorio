*** Settings ***
Resource  resource.robot
Test Setup  Create User    olduser    abcd5678

*** Test Cases ***
Register With Valid Username And Password
    Input New Command And Create User    test    abcd1234
    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    Input New Command And Create User    olduser    abcd1234
    Output Should Contain    User with username olduser already exists

Register With Too Short Username And Valid Password
    Input New Command And Create User    a    abcd1234
    Output Should Contain    Username must have only letters and at least 3 characters

Register With Enough Long But Invalid Username And Valid Password
    Input New Command And Create User    123    abcd1234
    Output Should Contain    Username must have only letters and at least 3 characters

Register With Valid Username And Too Short Password
    Input New Command And Create User    test    1234
    Output Should Contain   Password must have a non letter character and at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command And Create User    test    abcdefgh
    Output Should Contain   Password must have a non letter character and at least 8 characters

*** Keywords ***
Input New Command And Create User
    [Arguments]  ${username}  ${password}
    Input New Command
    Input Credentials    ${username}    ${password}