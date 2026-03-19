describe('Drug Discovery Data Engineering Prototype', () => {
  it('displays mock data from all sources', () => {
    cy.visit('http://localhost:3000');
    cy.contains('Drug Discovery Data Engineering Prototype');

    cy.contains('CDD Vault:').parent().should('contain', 'Compound: ABC123');
    cy.contains('Mosaic:').parent().should('contain', 'Sample: SMP456');
    cy.contains('Benchling:').parent().should('contain', 'Entry: ELN789');
  });
});
