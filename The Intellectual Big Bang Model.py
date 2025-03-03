import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import os
import time

# Start with only the fundamental principles
G_experiment = nx.Graph()
fundamental_principles = ["Relativity", "Flow & Emergence", "Fractal Symmetry"]
G_experiment.add_nodes_from(fundamental_principles)

# Directly defining the book categories (workaround for JSON issues)
categories = {
    "Religious Texts": [
        "The Bible", "The Quran", "The Bhagavad Gita", "The Tao Te Ching", "The Upanishads", "The Tibetan Book of the Dead"
    ],
    "Philosophy": [
        "The Republic", "Beyond Good and Evil", "Meditations", "Critique of Pure Reason",
        "The Consolation of Philosophy", "Thus Spoke Zarathustra", "The Phenomenology of Spirit"
    ],
    "Science & Mathematics": [
        "A Brief History of Time", "Gödel, Escher, Bach", "The Elegant Universe",
        "The Selfish Gene", "On the Origin of Species", "Quantum Mechanics and Path Integrals"
    ],
    "Literature & Mythology": [
        "The Lord of the Rings", "The Odyssey", "The Iliad", "Don Quixote",
        "The Divine Comedy", "The Poetics", "The Hero with a Thousand Faces"
    ],
    "Psychology & Human Nature": [
        "Thinking, Fast and Slow", "The Denial of Death", "Man’s Search for Meaning",
        "The Interpretation of Dreams", "The Lucifer Effect", "The Blank Slate"
    ],
    "Political & Economic Thought": [
        "The Prince", "Das Kapital", "The Wealth of Nations", "The Road to Serfdom",
        "The Social Contract", "Democracy in America"
    ]
}

# Additional books to expand knowledge space
additional_books = {
    "Modern Science & Technology": [
        "The Structure of Scientific Revolutions", "Chaos: Making a New Science", "The Singularity is Near"
    ],
    "Metaphysics & Mysticism": [
        "The Perennial Philosophy", "The Doors of Perception", "The Tao of Physics"
    ],
    "Sociology & Anthropology": [
        "Sapiens", "The Origins of Totalitarianism", "Discipline and Punish"
    ]
}

# Merge additional books into categories
categories.update(additional_books)

# Define book influence levels (weights)
influence_levels = {
    "Religious Texts": 3.5,
    "Philosophy": 2.8,
    "Science & Mathematics": 2.5,
    "Literature & Mythology": 2.3,
    "Psychology & Human Nature": 2.0,
    "Political & Economic Thought": 1.8,
    "Modern Science & Technology": 2.7,
    "Metaphysics & Mysticism": 3.0,
    "Sociology & Anthropology": 2.2
}

# Define intellectual "heat" (debate intensity)
controversial_books = {
    "Das Kapital": 5.0,
    "The Wealth of Nations": 5.0,
    "The Quran": 4.5,
    "The Bible": 4.5,
    "Beyond Good and Evil": 4.2,
    "The Prince": 5.0,
    "The Selfish Gene": 3.8,
    "The Interpretation of Dreams": 3.7,
    "Thinking, Fast and Slow": 3.5,
    "Sapiens": 4.0,
    "Discipline and Punish": 4.3
}

# Track books added over time
added_books = []

def add_book(book, category, step):
    if book not in G_experiment:
        G_experiment.add_node(book)
        added_books.append(book)
        
        # Apply dynamic weight based on influence level and controversy
        weight_factor = influence_levels.get(category, 2.0) * random.uniform(0.8, 1.2)
        heat_factor = controversial_books.get(book, 2.0)  # Default to 2.0 if not explicitly defined
        
        # Connect to fundamental principles probabilistically
        for principle in fundamental_principles:
            if random.random() < 0.8:  # Increased probability for better integration
                G_experiment.add_edge(book, principle, weight=weight_factor * heat_factor)
        
        # Connect to previously added books based on category influence
        category_connections = [b for b in added_books if random.random() < 0.4]  # Increased probability
        for connected_book in category_connections:
            connection_weight = weight_factor * heat_factor * random.uniform(0.8, 1.2)
            G_experiment.add_edge(book, connected_book, weight=connection_weight)

def visualize_experiment(title="Intellectual Big Bang - Knowledge Evolution (Thermodynamic Model)"):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G_experiment, seed=42, k=0.3)
    
    node_colors = ["orange" if node in fundamental_principles else "red" if node in categories["Religious Texts"] else "dodgerblue" for node in G_experiment.nodes]
    
    nx.draw(G_experiment, pos, with_labels=True, node_size=250, font_size=7, node_color=node_colors, edge_color="gray", alpha=0.7)
    plt.title(title)
    plt.show()

def run_experiment():
    global G_experiment
    G_experiment.clear()
    G_experiment.add_nodes_from(fundamental_principles)
    added_books.clear()
    
    for category, books in categories.items():
        for book in books:
            add_book(book, category, step=0)
    
    visualize_experiment()
    
    # Generate AI Suggestions
    most_connected_books = sorted(G_experiment.degree, key=lambda x: x[1], reverse=True)[:5]
    most_controversial = sorted(controversial_books.items(), key=lambda x: x[1], reverse=True)[:5]
    
    print("\n📌 Knowledge Gravity Centers: ", most_connected_books if most_connected_books else "None Found")
    print("📌 Most Controversial Books: ", most_controversial)
    
    # Print Thought Geodesic Example
    print("\n📌 Thought Geodesic:", find_knowledge_path("The Selfish Gene", "The Republic"))
    print("\nMischief managed! 🔥")

def find_knowledge_path(start_book, end_book):
    if start_book in G_experiment and end_book in G_experiment:
        try:
            path = nx.shortest_path(G_experiment, source=start_book, target=end_book, weight='weight')
            return " → ".join(path)
        except nx.NetworkXNoPath:
            return "No direct knowledge path found between these books."
    return "One or both books are not in the knowledge graph."

if __name__ == "__main__":
    run_experiment()

