/// <reference types="Cypress" />

describe("[Bmazon UI] User can", () => {
    it("create a new listing", ()=> {
        // Navigate to the create listing page.
        cy.visit("http://localhost:4200/");
        cy.get("[data-cy='create-new-listing-navlink']")
            .click();

        // Fill out listing data form.
        cy.get("[data-cy='listing-name-input']")
            .type("test - name");
        cy.get("[data-cy='listing-description-input']")
            .type("test - description");
        cy.get("[data-cy='listing-price-input']")
            .type("500");
        cy.get("[data-cy='listing-discount-input']")
            .type("1");
        cy.get("[data-cy='listing-supplier-input']")
            .type("1");
        cy.get("[data-cy='listing-category-input']")
            .type("1");
        cy.get("[data-cy='submit-listing-button']")
            .click();

        // Verify the new listing was created.
        cy.location("pathname")
            .should("eq", "/listings");
        cy.get("[data-cy='all-listings-container']").eq(-1)
            .invoke("text")
            .should("contain", "test - name")
            .and("contain", "500");
    });

    it("view the newly created listing", ()=> {
        // Navigate to the listing detail page.
        cy.visit("http://localhost:4200/");
        cy.get("[data-cy='listing-detail-link']").eq(-1)
            .click();

        // Verify the listing details of the newly created listing.
        cy.get("[data-cy='listing-detail-name']")
            .invoke("text")
            .should("contain", "test - name");
        cy.get("[data-cy='listing-detail-description']")
            .invoke("text")
            .should("contain", "test - description");
        cy.get("[data-cy='listing-detail-price']")
            .invoke("text")
            .should("contain", "500");
        cy.get("[data-cy='listing-detail-discount']")
            .invoke("text")
            .should("contain", "1");
        cy.get("[data-cy='listing-detail-supplier']")
            .invoke("text")
            .should("contain", "1");
        cy.get("[data-cy='listing-detail-category']")
            .invoke("text")
            .should("contain", "1");
    });
    
    it("edit the newly created listing", ()=> {
        // Navigate to the edit listing page.
        cy.visit("http://localhost:4200/");
        cy.get("[data-cy='listing-detail-link']").eq(-1)
            .click();
        cy.get("[data-cy='edit-listing-link']")
            .click();

        // Edit the newly created listing.
        cy.get("[data-cy='listing-name-input']")
            .clear()
            .type("test - edited name");
        cy.get("[data-cy='listing-description-input']")
            .clear()
            .type("test - edited description");
        cy.get("[data-cy='listing-price-input']")
            .clear()
            .type("1500");
        cy.get("[data-cy='listing-discount-input']")
            .clear()
            .type("2");
        cy.get("[data-cy='listing-supplier-input']")
            .clear()
            .type("2");
        cy.get("[data-cy='listing-category-input']")
            .clear()
            .type("2");
        cy.get("[data-cy='submit-listing-button']")
            .click();

        // Verify the edited details of the newly created listing.
        cy.location("pathname")
            .should("match", /^\/listings\/[0-9]+$/);
        cy.get("[data-cy='listing-detail-name']")
            .invoke("text")
            .should("contain", "test - edited name");
        cy.get("[data-cy='listing-detail-description']")
            .invoke("text")
            .should("contain", "test - edited description");
        cy.get("[data-cy='listing-detail-price']")
            .invoke("text")
            .should("contain", "1500");
        cy.get("[data-cy='listing-detail-discount']")
            .invoke("text")
            .should("contain", "2");
        cy.get("[data-cy='listing-detail-supplier']")
            .invoke("text")
            .should("contain", "2");
        cy.get("[data-cy='listing-detail-category']")
            .invoke("text")
            .should("contain", "2");
    });

    it("delete the newly created listing", ()=> {
        //Navigate to the create listing page.
        cy.visit("http://localhost:4200/");

        // Verify that the newly created listing exists.
        cy.get("[data-cy='all-listings-container']").eq(-1)
            .invoke("text")
            .should("contain", "test - edited name")
            .and("contain", "1500");

        // Delete the newly created listing.
        cy.get("[data-cy='delete-listing-button']").eq(-1)
            .click();

        // Verify that the newly created listing no longer exists.
        cy.get("[data-cy='listing-container']").eq(-1)
            .invoke("text")
            .should("not.contain", "test - edited name")
            .and("not.contain", "1500");
    });
});
