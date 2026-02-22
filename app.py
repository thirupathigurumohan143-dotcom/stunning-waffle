def recommend_style(occasion, weather, gender):
    occasion = occasion.lower()
    weather = weather.lower()
    gender = gender.lower()

    styles = {
        "casual": {
            "summer": {
                "male": "T-shirt + Shorts + Sneakers",
                "female": "Crop Top + Jeans/Skirt + Flats"
            },
            "winter": {
                "male": "Hoodie + Jeans + Boots",
                "female": "Sweater + Jeans + Ankle Boots"
            }
        },
        "formal": {
            "summer": {
                "male": "Light Shirt + Trousers + Loafers",
                "female": "Formal Blouse + Pencil Skirt + Heels"
            },
            "winter": {
                "male": "Blazer + Shirt + Formal Shoes",
                "female": "Coat + Formal Dress + Heels"
            }
        },
        "party": {
            "summer": {
                "male": "Slim Shirt + Chinos + Sneakers",
                "female": "One-piece Dress + Heels"
            },
            "winter": {
                "male": "Jacket + Black Jeans + Boots",
                "female": "Stylish Coat + Dress + Boots"
            }
        }
    }

    try:
        return styles[occasion][weather][gender]
    except KeyError:
        return "Style not found. Please check inputs."

if __name__ == "__main__":
    print("👗 Welcome to Fashion Style Recommender 👕")

    occasion = input("Enter Occasion (casual/formal/party): ")
    weather = input("Enter Weather (summer/winter): ")
    gender = input("Enter Gender (male/female): ")

    result = recommend_style(occasion, weather, gender)

    print("\n✨ Recommended Outfit:")
    print(result)
