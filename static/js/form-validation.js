// Validation du formulaire avec animations
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('quoteForm');
    
    if (!form) return;
    
    const inputs = form.querySelectorAll('.form-input');
    
    // Ajouter des animations au focus
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });
        
        input.addEventListener('blur', function() {
            this.parentElement.classList.remove('focused');
            validateInput(this);
        });
        
        input.addEventListener('input', function() {
            if (this.value.trim() !== '') {
                validateInput(this);
            }
        });
    });
    
    // Validation en temps réel
    function validateInput(input) {
        const value = input.value.trim();
        const formGroup = input.parentElement;
        
        // Supprimer les messages d'erreur existants
        const existingError = formGroup.querySelector('.error');
        if (existingError && !existingError.textContent.includes('Ce champ est obligatoire')) {
            existingError.remove();
        }
        
        // Validation email
        if (input.type === 'email' && value !== '') {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(value)) {
                showError(formGroup, 'Veuillez entrer une adresse email valide');
                input.classList.add('invalid');
                input.classList.remove('valid');
                return false;
            }
        }
        
        // Si tout est bon
        if (value !== '') {
            input.classList.remove('invalid');
            input.classList.add('valid');
        }
        
        return true;
    }
    
    function showError(formGroup, message) {
        const existingError = formGroup.querySelector('.error');
        if (!existingError || !existingError.textContent.includes('Ce champ est obligatoire')) {
            const error = document.createElement('span');
            error.className = 'error';
            error.textContent = message;
            formGroup.appendChild(error);
        }
    }
    
    // Validation à la soumission
    form.addEventListener('submit', function(e) {
        let isValid = true;
        
        inputs.forEach(input => {
            if (input.value.trim() === '') {
                isValid = false;
                input.classList.add('invalid');
            } else if (!validateInput(input)) {
                isValid = false;
            }
        });
        
        if (!isValid) {
            e.preventDefault();
            
            // Scroll vers le premier champ invalide
            const firstInvalid = form.querySelector('.invalid');
            if (firstInvalid) {
                firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
                firstInvalid.focus();
            }
        } else {
            // Ajouter un effet de chargement au bouton
            const submitButton = form.querySelector('.submit-button');
            submitButton.textContent = 'Chargement...';
            submitButton.disabled = true;
        }
    });
});
