//
//  UITestingTutorialUITests.swift
//  UITestingTutorialUITests
//
//  Created by Shifat Ahmed on 4/22/19.
//  Copyright © 2019 Code Pro. All rights reserved.
//

import XCTest

class UITestingTutorialUITests: XCTestCase {

    override func setUp() {
        // Put setup code here. This method is called before the invocation of each test method in the class.

        // In UI tests it is usually best to stop immediately when a failure occurs.
        continueAfterFailure = false

        // UI tests must launch the application that they test. Doing this in setup will make sure it happens for each test method.
        XCUIApplication().launch()

        // In UI tests it’s important to set the initial state - such as interface orientation - required for your tests before they run. The setUp method is a good place to do this.
    }
    
    func  testValidLoginSucess() {
        
        let validPassword = "abc123"
        let validUserName = "CodePro"
        let app = XCUIApplication()
        app.navigationBars["Mockify Music"].buttons["Profile"].tap()
        let userNameTextField = app.textFields["Username"]
        userNameTextField.tap()
        userNameTextField.typeText(validUserName)
        
        let passwordSecureTextField = app.secureTextFields["Password"]
        passwordSecureTextField.tap()
        passwordSecureTextField.typeText(validPassword)
        
        XCTAssertTrue(passwordSecureTextField.exists)
        XCTAssertTrue(userNameTextField.exists)
        
        
        passwordSecureTextField.tap()
        passwordSecureTextField.tap()
        passwordSecureTextField.tap()
        app.buttons["Login"].tap()
        
        
        
        
        
        
        
    }
    
    func test_option_buttons(){
        
        let tablesQuery = XCUIApplication().tables
        tablesQuery/*@START_MENU_TOKEN@*/.staticTexts["New Music"]/*[[".cells.staticTexts[\"New Music\"]",".staticTexts[\"New Music\"]"],[[[-1,1],[-1,0]]],[0]]@END_MENU_TOKEN@*/.tap()
        tablesQuery/*@START_MENU_TOKEN@*/.staticTexts["Just For You"]/*[[".cells.staticTexts[\"Just For You\"]",".staticTexts[\"Just For You\"]"],[[[-1,1],[-1,0]]],[0]]@END_MENU_TOKEN@*/.tap()
        tablesQuery/*@START_MENU_TOKEN@*/.staticTexts["Radio"]/*[[".cells.staticTexts[\"Radio\"]",".staticTexts[\"Radio\"]"],[[[-1,1],[-1,0]]],[0]]@END_MENU_TOKEN@*/.tap()
        
        let downloadCell = tablesQuery/*@START_MENU_TOKEN@*/.staticTexts["My Downloads"]/*[[".cells.staticTexts[\"My Downloads\"]",".staticTexts[\"My Downloads\"]"],[[[-1,1],[-1,0]]],[0]]@END_MENU_TOKEN@*/
        XCTAssertTrue(downloadCell.exists)
        
    }
    
    func test_wrong_passwoed(){
        
        let invalidPassword = "vulval"
        let invalidUserName = "000000"
        
        let app = XCUIApplication()
        app.navigationBars["Mockify Music"].buttons["Profile"].tap()
        app.textFields["Username"].tap()
        app.secureTextFields["Password"].tap()
        let loginbutton = app.buttons["Login"]
        XCTAssertTrue(loginbutton.exists)
        let alertDilog = app.alerts["Invalid Credentials"]
        XCTAssertFalse(alertDilog.exists)
       
        
    }
    
    func test_blank_login(){
        
        
        let app = XCUIApplication()
        app.navigationBars["Mockify Music"].buttons["Profile"].tap()
        app.buttons["Login"].tap()
        let alertDilog = app.alerts["Missing Credentials"]
        XCTAssertTrue(alertDilog.exists)
       
        
    }

    override func tearDown() {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
    }

    

}
