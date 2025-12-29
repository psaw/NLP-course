import json
import random

# Создаем разнообразный набор промптов для дистилляции
def generate_training_prompts(num_samples=500):
    """
    Генерирует разнообразный набор промптов для обучения LoRA адаптера
    """
    prompts = []

    # 1. Программирование и алгоритмы (30%)
    programming_templates = [
        "Write a Python function to {task}",
        "Implement a {data_structure} in Python with methods for {operations}",
        "Solve this coding problem: {problem}",
        "Explain how {algorithm} works with code example",
        "Debug this Python code: {code_snippet}"
    ]

    programming_tasks = [
        "calculate Fibonacci numbers iteratively",
        "check if a string is a palindrome",
        "find the maximum element in a list",
        "implement binary search",
        "reverse a linked list",
        "sort a list using quicksort",
        "detect cycles in a graph",
        "implement a stack data structure",
        "parse a mathematical expression",
        "generate all permutations of a string"
    ]

    # 2. Наука и математика (25%)
    science_templates = [
        "Explain {concept} in simple terms",
        "What is the difference between {concept1} and {concept2}?",
        "How does {process} work?",
        "Solve this math problem: {problem}",
        "What are the applications of {technology} in real life?"
    ]

    science_concepts = [
        "quantum entanglement",
        "photosynthesis",
        "machine learning",
        "blockchain technology",
        "neural networks",
        "climate change",
        "DNA replication",
        "black holes",
        "cryptography",
        "evolution by natural selection"
    ]

    # 3. Общие вопросы (25%)
    general_templates = [
        "What is {topic} and why is it important?",
        "Can you explain {concept} to a beginner?",
        "What are the main advantages and disadvantages of {thing}?",
        "How has {field} changed over the past decade?",
        "What should I know about {subject}?"
    ]

    general_topics = [
        "artificial intelligence",
        "renewable energy",
        "remote work",
        "cryptocurrency",
        "virtual reality",
        "electric vehicles",
        "social media",
        "cloud computing",
        "autonomous driving",
        "biotechnology"
    ]

    # 4. Креативные задачи (20%)
    creative_templates = [
        "Write a short story about {topic}",
        "Imagine you are {role}. How would you {action}?",
        "Create a recipe for {dish} with unusual ingredients",
        "Design a {object} for the future",
        "What would happen if {scenario}?"
    ]

    creative_topics = [
        "a robot learning emotions",
        "time travel to the dinosaur era",
        "a city underwater",
        "teleportation becoming reality",
        "animals that can talk",
        "a world without internet",
        "flying cars everywhere",
        "humans living on Mars"
    ]

    # Генерируем промпты по категориям
    num_programming = int(num_samples * 0.3)
    num_science = int(num_samples * 0.25)
    num_general = int(num_samples * 0.25)
    num_creative = num_samples - num_programming - num_science - num_general

    # Программирование
    for _ in range(num_programming):
        template = random.choice(programming_templates)
        if "{task}" in template:
            task = random.choice(programming_tasks)
            prompt = template.format(task=task)
        elif "{data_structure}" in template:
            structures = ["queue", "stack", "binary tree", "hash table", "graph"]
            operations = ["insert, delete, search", "push, pop, peek", "add, remove, traverse"]
            prompt = template.format(
                data_structure=random.choice(structures),
                operations=random.choice(operations)
            )
        elif "{algorithm}" in template:
            algorithms = ["Dijkstra's algorithm", "merge sort", "breadth-first search", "depth-first search"]
            prompt = template.format(algorithm=random.choice(algorithms))
        else:
            # Для других шаблонов используем общие задачи
            task = random.choice(programming_tasks)
            prompt = f"Write a Python function to {task}"
        prompts.append(prompt)

    # Наука и математика
    for _ in range(num_science):
        template = random.choice(science_templates)
        if "{concept}" in template:
            concept = random.choice(science_concepts)
            prompt = template.format(concept=concept)
        elif "{concept1}" in template and "{concept2}" in template:
            c1, c2 = random.sample(science_concepts, 2)
            prompt = template.format(concept1=c1, concept2=c2)
        elif "{process}" in template:
            processes = ["photosynthesis", "DNA replication", "neural transmission", "protein synthesis"]
            prompt = template.format(process=random.choice(processes))
        elif "{technology}" in template:
            technologies = ["machine learning", "blockchain", "quantum computing", "CRISPR"]
            prompt = template.format(technology=random.choice(technologies))
        else:
            concept = random.choice(science_concepts)
            prompt = f"Explain {concept} in simple terms"
        prompts.append(prompt)

    # Общие вопросы
    for _ in range(num_general):
        template = random.choice(general_templates)
        topic = random.choice(general_topics)
        if "{topic}" in template:
            prompt = template.format(topic=topic)
        elif "{concept}" in template:
            prompt = template.format(concept=topic)
        elif "{thing}" in template:
            prompt = template.format(thing=topic)
        elif "{field}" in template:
            prompt = template.format(field=topic)
        elif "{subject}" in template:
            prompt = template.format(subject=topic)
        else:
            prompt = f"What is {topic} and why is it important?"
        prompts.append(prompt)

    # Креативные задачи
    for _ in range(num_creative):
        template = random.choice(creative_templates)
        topic = random.choice(creative_topics)
        if "{topic}" in template:
            prompt = template.format(topic=topic)
        elif "{role}" in template and "{action}" in template:
            roles = ["a scientist", "an engineer", "a teacher", "a detective", "an artist"]
            actions = ["solve this mystery", "invent something new", "teach a complex concept", "explore unknown territory"]
            prompt = template.format(role=random.choice(roles), action=random.choice(actions))
        elif "{dish}" in template:
            dishes = ["chocolate cake", "pasta dish", "smoothie", "sandwich", "soup"]
            prompt = template.format(dish=random.choice(dishes))
        elif "{object}" in template:
            objects = ["smartphone", "house", "vehicle", "kitchen appliance", "toy"]
            prompt = template.format(object=random.choice(objects))
        elif "{scenario}" in template:
            scenarios = ["gravity disappeared", "everyone could read minds", "time stopped for everyone except you"]
            prompt = template.format(scenario=random.choice(scenarios))
        else:
            prompt = f"Write a short story about {topic}"
        prompts.append(prompt)

    # Перемешиваем промпты для разнообразия
    random.shuffle(prompts)

    return prompts

if __name__ == "__main__":
    # Генерируем промпты
    print("Генерируем обучающие промпты...")
    train_prompts = generate_training_prompts(num_samples=500)
    print(f"Сгенерировано {len(train_prompts)} промптов")

    # Показываем примеры
    print("\nПримеры промптов:")
    for i, prompt in enumerate(train_prompts[:5]):
        print(f"{i+1}. {prompt}")

    # Сохраняем промпты
    with open('train_prompts.json', 'w', encoding='utf-8') as f:
        json.dump(train_prompts, f, ensure_ascii=False, indent=2)
    print(f"\nПромпты сохранены в train_prompts.json")