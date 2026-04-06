// Mock Database Interaction (Simulating the Python Backend for UI Demo)
let companies = [];

// DOM Elements
const companyList = document.getElementById('company-list');
const addModal = document.getElementById('add-modal');
const btnAddCompany = document.getElementById('btn-add-company');
const closeModal = document.getElementById('close-modal');
const addCompanyForm = document.getElementById('add-company-form');
const totalCompaniesLabel = document.getElementById('total-companies');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    loadCompanies();
    setupEventListeners();
});

function setupEventListeners() {
    btnAddCompany.addEventListener('click', () => addModal.style.display = 'flex');
    closeModal.addEventListener('click', () => addModal.style.display = 'none');

    addCompanyForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const name = document.getElementById('comp-name').value;
        const niche = document.getElementById('comp-niche').value;
        const plan = document.getElementById('comp-plan').value;

        addCompany(name, niche, plan);
        addCompanyForm.reset();
        addModal.style.display = 'none';
    });
}

function loadCompanies() {
    // In a real app, we would fetch from the Python backend or a local API
    // For this demo, we use localStorage to persist UI state
    const saved = localStorage.getItem('instaConsult_companies');
    if (saved) {
        companies = JSON.parse(saved);
    } else {
        // Initial Empty State or Mock
        companies = [
            { id: '1', name: 'Greef Agency', niche: 'Marketing', plan: 'Enterprise', status: 'Active' }
        ];
        saveCompanies();
    }
    renderCompanies();
}

function saveCompanies() {
    localStorage.setItem('instaConsult_companies', JSON.stringify(companies));
    totalCompaniesLabel.textContent = companies.length;
}

function addCompany(name, niche, plan) {
    const newCompany = {
        id: Math.random().toString(36).substr(2, 9),
        name,
        niche,
        plan,
        status: 'Active'
    };
    companies.push(newCompany);
    saveCompanies();
    renderCompanies();
}

function deleteCompany(id) {
    if (confirm('Are you sure you want to delete this access?')) {
        companies = companies.filter(c => c.id !== id);
        saveCompanies();
        renderCompanies();
    }
}

function renderCompanies() {
    companyList.innerHTML = '';
    companies.forEach(company => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${company.id}</td>
            <td>${company.name}</td>
            <td>${company.niche}</td>
            <td>${company.plan}</td>
            <td><span class="status-badge">${company.status}</span></td>
            <td>
                <button class="btn-delete" onclick="deleteCompany('${company.id}')">Delete</button>
            </td>
        `;
        companyList.appendChild(tr);
    });
    totalCompaniesLabel.textContent = companies.length;
}

// Expose delete function to window for the onclick attribute
window.deleteCompany = deleteCompany;
