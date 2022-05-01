@web_tests
Feature: End to end web test feature

    @search @positive
    Scenario: Search an existing element
        Given I opened home page
        When I search "Dress" on Home page
        Then I see that search result counter is "more than 0"
        And I see that all elements contains text "Dress"

    @search @negative
    Scenario: Search non existing element
        Given I opened home page
        When I search "Perfumes" on Home page
        Then I see that search result counter is "0"
        And I see that No results message is shown
    
    @contact_us @positive
    Scenario: Send valid contact us form
        Given I opened home page
        When I send contact us request with subject: "Webmaster", email: "test@test.com", order_reference: "123456", message: "Hi from pytest", file: "image"
        Then I see that success contact us request was send