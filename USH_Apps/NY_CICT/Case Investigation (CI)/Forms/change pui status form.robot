*** Settings ***
Library  SeleniumLibrary
Resource    ../../Base/base.robot

*** Keywords ***
     

Convert Suspected Case to Confirmed Case
        Open Form    ${change pui status form}
        JS Click    ${suspected_to_confirmed_case}
        JS Click    ${confirm_suspected_to_confirmed_case}
        Submit Form and Check Success

