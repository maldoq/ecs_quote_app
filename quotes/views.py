from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse, Http404
from django.contrib import messages
from PIL import Image, ImageDraw, ImageFont
from django.core.files.base import ContentFile
from django.conf import settings
from .models import Quote, UserQuote
from .forms import UserQuoteForm
import io
import os
import random


def landing_page(request):
    """Vue pour la page d'accueil"""
    return render(request, 'landing.html')


def login_page(request):
    """Vue pour la page de connexion"""
    if request.method == 'POST':
        form = UserQuoteForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            # Vérifier si l'utilisateur existe déjà
            existing_user = UserQuote.objects.filter(email=email).first()
            
            if existing_user:
                # Rediriger vers sa carte existante
                return redirect('quote_card', user_id=existing_user.id)
            else:
                # Attribuer une citation aléatoire
                quotes = Quote.objects.all()
                if quotes.exists():
                    random_quote = random.choice(quotes)
                    user_quote = form.save(commit=False)
                    user_quote.quote = random_quote
                    user_quote.save()
                    return redirect('quote_card', user_id=user_quote.id)
                else:
                    messages.error(request, "Aucune citation disponible pour le moment.")
    else:
        form = UserQuoteForm()
    
    return render(request, 'login.html', {'form': form})


def quote_card(request, user_id):
    user_quote = get_object_or_404(UserQuote, id=user_id)

    if not user_quote.card_image:
        generate_card_image(user_quote)

    return render(request, 'quote_card.html', {
        'user_quote': user_quote
    })

def generate_card_image(user_quote):
    # Taille de la carte
    WIDTH, HEIGHT = 800, 500

    # Image de fond
    image = Image.new('RGB', (WIDTH, HEIGHT), '#1e3c72')
    draw = ImageDraw.Draw(image)

    # Police
    font_path = os.path.join(settings.BASE_DIR, 'static/fonts/arial.ttf')
    title_font = ImageFont.truetype(font_path, 36)
    text_font = ImageFont.truetype(font_path, 24)
    small_font = ImageFont.truetype(font_path, 20)

    # Texte
    draw.text((300, 40), "ECS 2026", fill='white', font=title_font)

    quote_text = f"❝ {user_quote.quote.text} ❞"
    draw.multiline_text(
        (60, 140),
        quote_text,
        fill='white',
        font=text_font,
        align='center',
        spacing=6
    )

    draw.text(
        (60, 260),
        f"— {user_quote.quote.author}",
        fill='#ffd700',
        font=small_font
    )

    draw.text(
        (60, 340),
        f"{user_quote.prenom} {user_quote.nom}",
        fill='white',
        font=text_font
    )

    draw.text(
        (60, 380),
        user_quote.ecole,
        fill='white',
        font=small_font
    )

    # Sauvegarde en mémoire
    buffer = io.BytesIO()
    image.save(buffer, format='PNG')

    # Enregistrer dans le champ ImageField
    user_quote.card_image.save(
        f'citation_{user_quote.id}.png',
        ContentFile(buffer.getvalue()),
        save=True
    )

def download_card(request, user_id):
    user_quote = get_object_or_404(UserQuote, id=user_id)

    # Générer l'image si elle n'existe pas encore
    if not user_quote.card_image:
        generate_card_image(user_quote)

    if not user_quote.card_image:
        raise Http404("Carte non disponible")

    file_path = user_quote.card_image.path

    return FileResponse(
        open(file_path, 'rb'),
        as_attachment=True,
        filename=f'citation_{user_quote.prenom}_{user_quote.nom}.png'
    )