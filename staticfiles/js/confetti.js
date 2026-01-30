// Fonction pour créer les confettis animés
document.addEventListener('DOMContentLoaded', function() {
    const confettiContainer = document.getElementById('confettiContainer');
    
    if (!confettiContainer) return;
    
    const colors = ['#FFD700', '#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F', '#BB8FCE'];
    const confettiCount = 50;
    
    function createConfetti() {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        
        // Position aléatoire
        confetti.style.left = Math.random() * 100 + '%';
        
        // Couleur aléatoire
        confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        
        // Taille aléatoire
        const size = Math.random() * 6 + 4;
        confetti.style.width = size + 'px';
        confetti.style.height = size + 'px';
        
        // Durée d'animation aléatoire
        const duration = Math.random() * 3 + 4;
        confetti.style.animationDuration = duration + 's';
        
        // Délai aléatoire
        const delay = Math.random() * 5;
        confetti.style.animationDelay = delay + 's';
        
        // Forme aléatoire (carré ou cercle)
        if (Math.random() > 0.5) {
            confetti.style.borderRadius = '50%';
        }
        
        confettiContainer.appendChild(confetti);
        
        // Supprimer le confetti après l'animation
        setTimeout(() => {
            if (confetti && confetti.parentNode) {
                confetti.parentNode.removeChild(confetti);
            }
        }, (duration + delay) * 1000);
    }
    
    // Créer les confettis initiaux
    for (let i = 0; i < confettiCount; i++) {
        setTimeout(() => createConfetti(), i * 100);
    }
    
    // Continuer à créer des confettis périodiquement
    setInterval(() => {
        createConfetti();
    }, 300);
});