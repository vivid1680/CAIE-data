import csv
import os

def append_to_csv(filepath, row):
    with open(filepath, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

def update_topics():
    print("Updating topics.csv...")
    existing_topics = set()
    if os.path.exists('data/topics.csv'):
        with open('data/topics.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None) # skip header
            for row in reader:
                if row:
                    existing_topics.add((row[0], row[1]))

    topics = [
        ['9709', 'Quadratics'],
        ['9709', 'Functions'],
        ['9709', 'Coordinate Geometry'],
        ['9709', 'Circular Measure'],
        ['9709', 'Trigonometry'],
        ['9709', 'Series'],
        ['9709', 'Differentiation'],
        ['9709', 'Integration'],
        ['9709', 'Algebra'],
        ['9709', 'Logarithmic and Exponential Functions'],
        ['9709', 'Numerical Solutions of Equations'],
        ['9709', 'Vectors'],
        ['9709', 'Differential Equations'],
        ['9709', 'Complex Numbers'],
        ['9709', 'Representation of Data'],
        ['9709', 'Permutations and Combinations'],
        ['9709', 'Probability'],
        ['9709', 'Discrete Random Variables'],
        ['9709', 'The Normal Distribution']
    ]
    for t in topics:
        if (t[0], t[1]) not in existing_topics:
            append_to_csv('data/topics.csv', t)

def update_question_topics():
    print("Updating question_topics.csv...")
    # subject_code,year,session,paper_number,variant,question_number,topic_name
    
    # 9709 November 2025 Variant 11 (P1)
    q_topics_11 = [
        ['9709', '2025', 'November', '1', '1', '1', 'Series'],
        ['9709', '2025', 'November', '1', '1', '2', 'Series'],
        ['9709', '2025', 'November', '1', '1', '3', 'Series'],
        ['9709', '2025', 'November', '1', '1', '4', 'Quadratics'],
        ['9709', '2025', 'November', '1', '1', '5', 'Trigonometry'],
        ['9709', '2025', 'November', '1', '1', '6', 'Functions'],
        ['9709', '2025', 'November', '1', '1', '7', 'Circular Measure'],
        ['9709', '2025', 'November', '1', '1', '8', 'Integration'],
        ['9709', '2025', 'November', '1', '1', '9', 'Series'],
        ['9709', '2025', 'November', '1', '1', '10', 'Coordinate Geometry'],
        ['9709', '2025', 'November', '1', '1', '11', 'Differentiation']
    ]
    
    # 9709 November 2025 Variant 31 (P3)
    q_topics_31 = [
        ['9709', '2025', 'November', '3', '1', '1', 'Algebra'],
        ['9709', '2025', 'November', '3', '1', '2', 'Complex Numbers'],
        ['9709', '2025', 'November', '3', '1', '3', 'Algebra'],
        ['9709', '2025', 'November', '3', '1', '4', 'Vectors'],
        ['9709', '2025', 'November', '3', '1', '9', 'Numerical Solutions of Equations']
    ]
    
    # 9709 November 2025 Variant 51 (S1)
    q_topics_51 = [
        ['9709', '2025', 'November', '5', '1', '1', 'Discrete Random Variables'],
        ['9709', '2025', 'November', '5', '1', '2', 'Discrete Random Variables'],
        ['9709', '2025', 'November', '5', '1', '4', 'Probability'],
        ['9709', '2025', 'November', '5', '1', '5', 'The Normal Distribution'],
        ['9709', '2025', 'November', '5', '1', '6', 'The Normal Distribution'],
        ['9709', '2025', 'November', '5', '1', '7', 'Permutations and Combinations'],
        ['9709', '2025', 'November', '5', '1', '11', 'Permutations and Combinations']
    ]

    # 9709 November 2025 Variant 12 (P1)
    q_topics_12 = [
        ['9709', '2025', 'November', '1', '2', '1', 'Trigonometry'],
        ['9709', '2025', 'November', '1', '2', '2', 'Differentiation'],
        ['9709', '2025', 'November', '1', '2', '3', 'Series'],
        ['9709', '2025', 'November', '1', '2', '4', 'Integration'],
        ['9709', '2025', 'November', '1', '2', '5', 'Quadratics'],
        ['9709', '2025', 'November', '1', '2', '6', 'Coordinate Geometry'],
        ['9709', '2025', 'November', '1', '2', '7', 'Circular Measure'],
        ['9709', '2025', 'November', '1', '2', '8', 'Series'],
        ['9709', '2025', 'November', '1', '2', '9', 'Differentiation']
    ]

    # 9709 November 2025 Variant 32 (P3)
    q_topics_32 = [
        ['9709', '2025', 'November', '3', '2', '1', 'Algebra'],
        ['9709', '2025', 'November', '3', '2', '2', 'Complex Numbers'],
        ['9709', '2025', 'November', '3', '2', '3', 'Logarithmic and Exponential Functions'],
        ['9709', '2025', 'November', '3', '2', '4', 'Vectors'],
        ['9709', '2025', 'November', '3', '2', '5', 'Differential Equations'],
        ['9709', '2025', 'November', '3', '2', '6', 'Integration'],
        ['9709', '2025', 'November', '3', '2', '7', 'Trigonometry'],
        ['9709', '2025', 'November', '3', '2', '8', 'Numerical Solutions of Equations'],
        ['9709', '2025', 'November', '3', '2', '9', 'Differentiation']
    ]

    # 9709 November 2025 Variant 52 (S1)
    q_topics_52 = [
        ['9709', '2025', 'November', '5', '2', '1', 'Representation of Data'],
        ['9709', '2025', 'November', '5', '2', '2', 'Probability'],
        ['9709', '2025', 'November', '5', '2', '3', 'Discrete Random Variables'],
        ['9709', '2025', 'November', '5', '2', '4', 'Permutations and Combinations'],
        ['9709', '2025', 'November', '5', '2', '5', 'The Normal Distribution'],
        ['9709', '2025', 'November', '5', '2', '6', 'The Normal Distribution'],
        ['9709', '2025', 'November', '5', '2', '7', 'Probability']
    ]
    
    # 9709 November 2025 Variant 13 (P1)
    q_topics_13 = [
        ['9709', '2025', 'November', '1', '3', '1', 'Series'],
        ['9709', '2025', 'November', '1', '3', '2', 'Differentiation'],
        ['9709', '2025', 'November', '1', '3', '3', 'Circular Measure'],
        ['9709', '2025', 'November', '1', '3', '4', 'Trigonometry'],
        ['9709', '2025', 'November', '1', '3', '5', 'Integration'],
        ['9709', '2025', 'November', '1', '3', '6', 'Functions'],
        ['9709', '2025', 'November', '1', '3', '7', 'Differentiation'],
        ['9709', '2025', 'November', '1', '3', '8', 'Coordinate Geometry']
    ]

    # 9709 November 2025 Variant 23 (P2)
    q_topics_23 = [
        ['9709', '2025', 'November', '2', '3', '1', 'Algebra'],
        ['9709', '2025', 'November', '2', '3', '2', 'Logarithmic and Exponential Functions'],
        ['9709', '2025', 'November', '2', '3', '3', 'Trigonometry'],
        ['9709', '2025', 'November', '2', '3', '4', 'Differentiation'],
        ['9709', '2025', 'November', '2', '3', '5', 'Integration'],
        ['9709', '2025', 'November', '2', '3', '6', 'Numerical Solutions of Equations'],
        ['9709', '2025', 'November', '2', '3', '7', 'Differentiation'],
        ['9709', '2025', 'November', '2', '3', '8', 'Integration']
    ]

    # 9709 November 2025 Variant 53 (S1)
    q_topics_53 = [
        ['9709', '2025', 'November', '5', '3', '1', 'Representation of Data'],
        ['9709', '2025', 'November', '5', '3', '2', 'Probability'],
        ['9709', '2025', 'November', '5', '3', '3', 'Permutations and Combinations'],
        ['9709', '2025', 'November', '5', '3', '4', 'Discrete Random Variables'],
        ['9709', '2025', 'November', '5', '3', '5', 'The Normal Distribution'],
        ['9709', '2025', 'November', '5', '3', '6', 'The Normal Distribution'],
        ['9709', '2025', 'November', '5', '3', '7', 'Probability']
    ]
    
    # 9709 June 2025 Variant 11 (P1)
    q_topics_s25_11 = [
        ['9709', '2025', 'June', '1', '1', '1', 'Series'],
        ['9709', '2025', 'June', '1', '1', '2', 'Quadratics'],
        ['9709', '2025', 'June', '1', '1', '3', 'Differentiation'],
        ['9709', '2025', 'June', '1', '1', '4', 'Circular Measure'],
        ['9709', '2025', 'June', '1', '1', '5', 'Trigonometry'],
        ['9709', '2025', 'June', '1', '1', '6', 'Functions'],
        ['9709', '2025', 'June', '1', '1', '7', 'Integration'],
        ['9709', '2025', 'June', '1', '1', '8', 'Series'],
        ['9709', '2025', 'June', '1', '1', '9', 'Coordinate Geometry']
    ]

    # 9709 June 2025 Variant 31 (P3)
    q_topics_s25_31 = [
        ['9709', '2025', 'June', '3', '1', '1', 'Algebra'],
        ['9709', '2025', 'June', '3', '1', '2', 'Complex Numbers'],
        ['9709', '2025', 'June', '3', '1', '3', 'Logarithmic and Exponential Functions'],
        ['9709', '2025', 'June', '3', '1', '4', 'Vectors'],
        ['9709', '2025', 'June', '3', '1', '5', 'Differential Equations'],
        ['9709', '2025', 'June', '3', '1', '6', 'Integration'],
        ['9709', '2025', 'June', '3', '1', '7', 'Trigonometry'],
        ['9709', '2025', 'June', '3', '1', '8', 'Numerical Solutions of Equations'],
        ['9709', '2025', 'June', '3', '1', '9', 'Differentiation']
    ]

    # 9709 June 2025 Variant 51 (S1)
    q_topics_s25_51 = [
        ['9709', '2025', 'June', '5', '1', '1', 'Representation of Data'],
        ['9709', '2025', 'June', '5', '1', '2', 'Probability'],
        ['9709', '2025', 'June', '5', '1', '3', 'Discrete Random Variables'],
        ['9709', '2025', 'June', '5', '1', '4', 'Permutations and Combinations'],
        ['9709', '2025', 'June', '5', '1', '5', 'The Normal Distribution'],
        ['9709', '2025', 'June', '5', '1', '6', 'The Normal Distribution'],
        ['9709', '2025', 'June', '5', '1', '7', 'Probability']
    ]
    
    # 9709 June 2025 Variant 12 (P1)
    q_topics_s25_12 = [
        ['9709', '2025', 'June', '1', '2', '1', 'Series'],
        ['9709', '2025', 'June', '1', '2', '2', 'Differentiation'],
        ['9709', '2025', 'June', '1', '2', '3', 'Circular Measure'],
        ['9709', '2025', 'June', '1', '2', '4', 'Trigonometry'],
        ['9709', '2025', 'June', '1', '2', '5', 'Integration'],
        ['9709', '2025', 'June', '1', '2', '6', 'Functions'],
        ['9709', '2025', 'June', '1', '2', '7', 'Differentiation'],
        ['9709', '2025', 'June', '1', '2', '8', 'Coordinate Geometry'],
        ['9709', '2025', 'June', '1', '2', '9', 'Differentiation']
    ]

    # 9709 June 2025 Variant 32 (P3)
    q_topics_s25_32 = [
        ['9709', '2025', 'June', '3', '2', '1', 'Algebra'],
        ['9709', '2025', 'June', '3', '2', '2', 'Complex Numbers'],
        ['9709', '2025', 'June', '3', '2', '3', 'Logarithmic and Exponential Functions'],
        ['9709', '2025', 'June', '3', '2', '4', 'Vectors'],
        ['9709', '2025', 'June', '3', '2', '5', 'Differential Equations'],
        ['9709', '2025', 'June', '3', '2', '6', 'Integration'],
        ['9709', '2025', 'June', '3', '2', '7', 'Trigonometry'],
        ['9709', '2025', 'June', '3', '2', '8', 'Numerical Solutions of Equations'],
        ['9709', '2025', 'June', '3', '2', '9', 'Differentiation']
    ]

    # 9709 June 2025 Variant 52 (S1)
    q_topics_s25_52 = [
        ['9709', '2025', 'June', '5', '2', '1', 'Representation of Data'],
        ['9709', '2025', 'June', '5', '2', '2', 'Probability'],
        ['9709', '2025', 'June', '5', '2', '3', 'Discrete Random Variables'],
        ['9709', '2025', 'June', '5', '2', '4', 'Permutations and Combinations'],
        ['9709', '2025', 'June', '5', '2', '5', 'The Normal Distribution'],
        ['9709', '2025', 'June', '5', '2', '6', 'The Normal Distribution'],
        ['9709', '2025', 'June', '5', '2', '7', 'Probability']
    ]
    
    # 9709 June 2025 Variant 13 (P1)
    q_topics_s25_13 = [
        ['9709', '2025', 'June', '1', '3', '1', 'Series'],
        ['9709', '2025', 'June', '1', '3', '2', 'Differentiation'],
        ['9709', '2025', 'June', '1', '3', '3', 'Circular Measure'],
        ['9709', '2025', 'June', '1', '3', '4', 'Trigonometry'],
        ['9709', '2025', 'June', '1', '3', '5', 'Integration'],
        ['9709', '2025', 'June', '1', '3', '6', 'Functions'],
        ['9709', '2025', 'June', '1', '3', '7', 'Differentiation'],
        ['9709', '2025', 'June', '1', '3', '8', 'Coordinate Geometry'],
        ['9709', '2025', 'June', '1', '3', '9', 'Differentiation'],
        ['9709', '2025', 'June', '1', '3', '10', 'Integration'],
        ['9709', '2025', 'June', '1', '3', '11', 'Trigonometry'],
        ['9709', '2025', 'June', '1', '3', '12', 'Coordinate Geometry']
    ]

    # 9709 June 2025 Variant 33 (P3)
    q_topics_s25_33 = [
        ['9709', '2025', 'June', '3', '3', '1', 'Algebra'],
        ['9709', '2025', 'June', '3', '3', '2', 'Complex Numbers'],
        ['9709', '2025', 'June', '3', '3', '3', 'Logarithmic and Exponential Functions'],
        ['9709', '2025', 'June', '3', '3', '4', 'Vectors'],
        ['9709', '2025', 'June', '3', '3', '5', 'Differential Equations'],
        ['9709', '2025', 'June', '3', '3', '6', 'Integration'],
        ['9709', '2025', 'June', '3', '3', '7', 'Trigonometry'],
        ['9709', '2025', 'June', '3', '3', '8', 'Numerical Solutions of Equations'],
        ['9709', '2025', 'June', '3', '3', '9', 'Differentiation'],
        ['9709', '2025', 'June', '3', '3', '10', 'Algebra']
    ]

    # 9709 June 2025 Variant 53 (S1)
    q_topics_s25_53 = [
        ['9709', '2025', 'June', '5', '3', '1', 'Representation of Data'],
        ['9709', '2025', 'June', '5', '3', '2', 'Probability'],
        ['9709', '2025', 'June', '5', '3', '3', 'Discrete Random Variables'],
        ['9709', '2025', 'June', '5', '3', '4', 'Permutations and Combinations'],
        ['9709', '2025', 'June', '5', '3', '5', 'The Normal Distribution'],
        ['9709', '2025', 'June', '5', '3', '6', 'The Normal Distribution'],
        ['9709', '2025', 'June', '5', '3', '7', 'Probability']
    ]
    
    # 9709 March 2025 Variant 12 (P1)
    q_topics_m25_12 = [
        ['9709', '2025', 'March', '1', '2', '1', 'Series'],
        ['9709', '2025', 'March', '1', '2', '2', 'Differentiation'],
        ['9709', '2025', 'March', '1', '2', '3', 'Circular Measure'],
        ['9709', '2025', 'March', '1', '2', '4', 'Trigonometry'],
        ['9709', '2025', 'March', '1', '2', '5', 'Integration'],
        ['9709', '2025', 'March', '1', '2', '6', 'Functions'],
        ['9709', '2025', 'March', '1', '2', '7', 'Differentiation'],
        ['9709', '2025', 'March', '1', '2', '8', 'Coordinate Geometry'],
        ['9709', '2025', 'March', '1', '2', '9', 'Integration'],
        ['9709', '2025', 'March', '1', '2', '10', 'Trigonometry'],
        ['9709', '2025', 'March', '1', '2', '11', 'Coordinate Geometry']
    ]

    # 9709 March 2025 Variant 32 (P3)
    q_topics_m25_32 = [
        ['9709', '2025', 'March', '3', '2', '1', 'Algebra'],
        ['9709', '2025', 'March', '3', '2', '2', 'Complex Numbers'],
        ['9709', '2025', 'March', '3', '2', '3', 'Logarithmic and Exponential Functions'],
        ['9709', '2025', 'March', '3', '2', '4', 'Vectors'],
        ['9709', '2025', 'March', '3', '2', '5', 'Differential Equations'],
        ['9709', '2025', 'March', '3', '2', '6', 'Integration'],
        ['9709', '2025', 'March', '3', '2', '7', 'Trigonometry'],
        ['9709', '2025', 'March', '3', '2', '8', 'Numerical Solutions of Equations'],
        ['9709', '2025', 'March', '3', '2', '9', 'Differentiation'],
        ['9709', '2025', 'March', '3', '2', '10', 'Complex Numbers']
    ]

    # 9709 March 2025 Variant 52 (S1)
    q_topics_m25_52 = [
        ['9709', '2025', 'March', '5', '2', '1', 'Representation of Data'],
        ['9709', '2025', 'March', '5', '2', '2', 'Probability'],
        ['9709', '2025', 'March', '5', '2', '3', 'Discrete Random Variables'],
        ['9709', '2025', 'March', '5', '2', '4', 'Permutations and Combinations'],
        ['9709', '2025', 'March', '5', '2', '5', 'The Normal Distribution'],
        ['9709', '2025', 'March', '5', '2', '6', 'The Normal Distribution'],
        ['9709', '2025', 'March', '5', '2', '7', 'Probability']
    ]
    
    # 9709 November 2024 Variant 11 (P1)
    q_topics_w24_11 = [
        ['9709', '2024', 'November', '1', '1', '1', 'Series'],
        ['9709', '2024', 'November', '1', '1', '2', 'Differentiation'],
        ['9709', '2024', 'November', '1', '1', '3', 'Circular Measure'],
        ['9709', '2024', 'November', '1', '1', '4', 'Trigonometry'],
        ['9709', '2024', 'November', '1', '1', '5', 'Integration'],
        ['9709', '2024', 'November', '1', '1', '6', 'Functions'],
        ['9709', '2024', 'November', '1', '1', '7', 'Differentiation'],
        ['9709', '2024', 'November', '1', '1', '8', 'Coordinate Geometry'],
        ['9709', '2024', 'November', '1', '1', '9', 'Integration'],
        ['9709', '2024', 'November', '1', '1', '10', 'Trigonometry'],
        ['9709', '2024', 'November', '1', '1', '11', 'Coordinate Geometry']
    ]

    # 9709 November 2024 Variant 31 (P3)
    q_topics_w24_31 = [
        ['9709', '2024', 'November', '3', '1', '1', 'Algebra'],
        ['9709', '2024', 'November', '3', '1', '2', 'Complex Numbers'],
        ['9709', '2024', 'November', '3', '1', '3', 'Logarithmic and Exponential Functions'],
        ['9709', '2024', 'November', '3', '1', '4', 'Vectors'],
        ['9709', '2024', 'November', '3', '1', '5', 'Differential Equations'],
        ['9709', '2024', 'November', '3', '1', '6', 'Integration'],
        ['9709', '2024', 'November', '3', '1', '7', 'Trigonometry'],
        ['9709', '2024', 'November', '3', '1', '8', 'Numerical Solutions of Equations'],
        ['9709', '2024', 'November', '3', '1', '9', 'Differentiation'],
        ['9709', '2024', 'November', '3', '1', '10', 'Complex Numbers']
    ]

    # 9709 November 2024 Variant 51 (S1)
    q_topics_w24_51 = [
        ['9709', '2024', 'November', '5', '1', '1', 'Representation of Data'],
        ['9709', '2024', 'November', '5', '1', '2', 'Probability'],
        ['9709', '2024', 'November', '5', '1', '3', 'Discrete Random Variables'],
        ['9709', '2024', 'November', '5', '1', '4', 'Permutations and Combinations'],
        ['9709', '2024', 'November', '5', '1', '5', 'The Normal Distribution'],
        ['9709', '2024', 'November', '5', '1', '6', 'The Normal Distribution'],
        ['9709', '2024', 'November', '5', '1', '7', 'Probability']
    ]
    
    # 9709 November 2024 Variant 12 (P1)
    q_topics_w24_12 = [
        ['9709', '2024', 'November', '1', '2', '1', 'Series'],
        ['9709', '2024', 'November', '1', '2', '2', 'Differentiation'],
        ['9709', '2024', 'November', '1', '2', '3', 'Circular Measure'],
        ['9709', '2024', 'November', '1', '2', '4', 'Trigonometry'],
        ['9709', '2024', 'November', '1', '2', '5', 'Integration'],
        ['9709', '2024', 'November', '1', '2', '6', 'Functions'],
        ['9709', '2024', 'November', '1', '2', '7', 'Differentiation'],
        ['9709', '2024', 'November', '1', '2', '8', 'Coordinate Geometry'],
        ['9709', '2024', 'November', '1', '2', '9', 'Integration'],
        ['9709', '2024', 'November', '1', '2', '10', 'Trigonometry'],
        ['9709', '2024', 'November', '1', '2', '11', 'Coordinate Geometry']
    ]

    # 9709 November 2024 Variant 32 (P3)
    q_topics_w24_32 = [
        ['9709', '2024', 'November', '3', '2', '1', 'Algebra'],
        ['9709', '2024', 'November', '3', '2', '2', 'Complex Numbers'],
        ['9709', '2024', 'November', '3', '2', '3', 'Logarithmic and Exponential Functions'],
        ['9709', '2024', 'November', '3', '2', '4', 'Vectors'],
        ['9709', '2024', 'November', '3', '2', '5', 'Differential Equations'],
        ['9709', '2024', 'November', '3', '2', '6', 'Integration'],
        ['9709', '2024', 'November', '3', '2', '7', 'Trigonometry'],
        ['9709', '2024', 'November', '3', '2', '8', 'Numerical Solutions of Equations'],
        ['9709', '2024', 'November', '3', '2', '9', 'Differentiation'],
        ['9709', '2024', 'November', '3', '2', '10', 'Complex Numbers'],
        ['9709', '2024', 'November', '3', '2', '11', 'Vectors']
    ]

    # 9709 November 2024 Variant 52 (S1)
    q_topics_w24_52 = [
        ['9709', '2024', 'November', '5', '2', '1', 'Representation of Data'],
        ['9709', '2024', 'November', '5', '2', '2', 'Probability'],
        ['9709', '2024', 'November', '5', '2', '3', 'Discrete Random Variables'],
        ['9709', '2024', 'November', '5', '2', '4', 'Permutations and Combinations'],
        ['9709', '2024', 'November', '5', '2', '5', 'The Normal Distribution'],
        ['9709', '2024', 'November', '5', '2', '6', 'The Normal Distribution'],
        ['9709', '2024', 'November', '5', '2', '7', 'Probability']
    ]
    
    # 9709 November 2024 Variant 13 (P1)
    q_topics_w24_13 = [
        ['9709', '2024', 'November', '1', '3', '1', 'Series'],
        ['9709', '2024', 'November', '1', '3', '2', 'Differentiation'],
        ['9709', '2024', 'November', '1', '3', '3', 'Circular Measure'],
        ['9709', '2024', 'November', '1', '3', '4', 'Trigonometry'],
        ['9709', '2024', 'November', '1', '3', '5', 'Integration'],
        ['9709', '2024', 'November', '1', '3', '6', 'Functions'],
        ['9709', '2024', 'November', '1', '3', '7', 'Differentiation'],
        ['9709', '2024', 'November', '1', '3', '8', 'Coordinate Geometry'],
        ['9709', '2024', 'November', '1', '3', '9', 'Integration'],
        ['9709', '2024', 'November', '1', '3', '10', 'Trigonometry'],
        ['9709', '2024', 'November', '1', '3', '11', 'Coordinate Geometry']
    ]

    # 9709 November 2024 Variant 33 (P3)
    q_topics_w24_33 = [
        ['9709', '2024', 'November', '3', '3', '1', 'Algebra'],
        ['9709', '2024', 'November', '3', '3', '2', 'Complex Numbers'],
        ['9709', '2024', 'November', '3', '3', '3', 'Logarithmic and Exponential Functions'],
        ['9709', '2024', 'November', '3', '3', '4', 'Vectors'],
        ['9709', '2024', 'November', '3', '3', '5', 'Differential Equations'],
        ['9709', '2024', 'November', '3', '3', '6', 'Integration'],
        ['9709', '2024', 'November', '3', '3', '7', 'Trigonometry'],
        ['9709', '2024', 'November', '3', '3', '8', 'Numerical Solutions of Equations'],
        ['9709', '2024', 'November', '3', '3', '9', 'Differentiation'],
        ['9709', '2024', 'November', '3', '3', '10', 'Complex Numbers']
    ]

    # 9709 November 2024 Variant 53 (S1)
    q_topics_w24_53 = [
        ['9709', '2024', 'November', '5', '3', '1', 'Representation of Data'],
        ['9709', '2024', 'November', '5', '3', '2', 'Probability'],
        ['9709', '2024', 'November', '5', '3', '3', 'Discrete Random Variables'],
        ['9709', '2024', 'November', '5', '3', '4', 'Permutations and Combinations'],
        ['9709', '2024', 'November', '5', '3', '5', 'The Normal Distribution'],
        ['9709', '2024', 'November', '5', '3', '6', 'The Normal Distribution'],
        ['9709', '2024', 'November', '5', '3', '7', 'Probability']
    ]
    
    # 9709 June 2024 Variant 11 (P1)
    q_topics_s24_11 = [
        ['9709', '2024', 'June', '1', '1', '1', 'Series'],
        ['9709', '2024', 'June', '1', '1', '2', 'Differentiation'],
        ['9709', '2024', 'June', '1', '1', '3', 'Circular Measure'],
        ['9709', '2024', 'June', '1', '1', '4', 'Trigonometry'],
        ['9709', '2024', 'June', '1', '1', '5', 'Integration'],
        ['9709', '2024', 'June', '1', '1', '6', 'Functions'],
        ['9709', '2024', 'June', '1', '1', '7', 'Differentiation'],
        ['9709', '2024', 'June', '1', '1', '8', 'Coordinate Geometry'],
        ['9709', '2024', 'June', '1', '1', '9', 'Integration'],
        ['9709', '2024', 'June', '1', '1', '10', 'Trigonometry'],
        ['9709', '2024', 'June', '1', '1', '11', 'Coordinate Geometry']
    ]

    # 9709 June 2024 Variant 31 (P3)
    q_topics_s24_31 = [
        ['9709', '2024', 'June', '3', '1', '1', 'Algebra'],
        ['9709', '2024', 'June', '3', '1', '2', 'Complex Numbers'],
        ['9709', '2024', 'June', '3', '1', '3', 'Logarithmic and Exponential Functions'],
        ['9709', '2024', 'June', '3', '1', '4', 'Vectors'],
        ['9709', '2024', 'June', '3', '1', '5', 'Differential Equations'],
        ['9709', '2024', 'June', '3', '1', '6', 'Integration'],
        ['9709', '2024', 'June', '3', '1', '7', 'Trigonometry'],
        ['9709', '2024', 'June', '3', '1', '8', 'Numerical Solutions of Equations'],
        ['9709', '2024', 'June', '3', '1', '9', 'Differentiation'],
        ['9709', '2024', 'June', '3', '1', '10', 'Complex Numbers']
    ]

    # 9709 June 2024 Variant 51 (S1)
    q_topics_s24_51 = [
        ['9709', '2024', 'June', '5', '1', '1', 'Representation of Data'],
        ['9709', '2024', 'June', '5', '1', '2', 'Probability'],
        ['9709', '2024', 'June', '5', '1', '3', 'Discrete Random Variables'],
        ['9709', '2024', 'June', '5', '1', '4', 'Permutations and Combinations'],
        ['9709', '2024', 'June', '5', '1', '5', 'The Normal Distribution'],
        ['9709', '2024', 'June', '5', '1', '6', 'The Normal Distribution'],
        ['9709', '2024', 'June', '5', '1', '7', 'Probability']
    ]
    
    # 9709 June 2024 Variant 12 (P1)
    q_topics_s24_12 = [
        ['9709', '2024', 'June', '1', '2', '1', 'Series'],
        ['9709', '2024', 'June', '1', '2', '2', 'Differentiation'],
        ['9709', '2024', 'June', '1', '2', '3', 'Circular Measure'],
        ['9709', '2024', 'June', '1', '2', '4', 'Trigonometry'],
        ['9709', '2024', 'June', '1', '2', '5', 'Integration'],
        ['9709', '2024', 'June', '1', '2', '6', 'Functions'],
        ['9709', '2024', 'June', '1', '2', '7', 'Differentiation'],
        ['9709', '2024', 'June', '1', '2', '8', 'Coordinate Geometry'],
        ['9709', '2024', 'June', '1', '2', '9', 'Integration'],
        ['9709', '2024', 'June', '1', '2', '10', 'Trigonometry'],
        ['9709', '2024', 'June', '1', '2', '11', 'Coordinate Geometry']
    ]

    # 9709 June 2024 Variant 32 (P3)
    q_topics_s24_32 = [
        ['9709', '2024', 'June', '3', '2', '1', 'Algebra'],
        ['9709', '2024', 'June', '3', '2', '2', 'Complex Numbers'],
        ['9709', '2024', 'June', '3', '2', '3', 'Logarithmic and Exponential Functions'],
        ['9709', '2024', 'June', '3', '2', '4', 'Vectors'],
        ['9709', '2024', 'June', '3', '2', '5', 'Differential Equations'],
        ['9709', '2024', 'June', '3', '2', '6', 'Integration'],
        ['9709', '2024', 'June', '3', '2', '7', 'Trigonometry'],
        ['9709', '2024', 'June', '3', '2', '8', 'Numerical Solutions of Equations'],
        ['9709', '2024', 'June', '3', '2', '9', 'Differentiation'],
        ['9709', '2024', 'June', '3', '2', '10', 'Complex Numbers']
    ]

    # 9709 June 2024 Variant 52 (S1)
    q_topics_s24_52 = [
        ['9709', '2024', 'June', '5', '2', '1', 'Representation of Data'],
        ['9709', '2024', 'June', '5', '2', '2', 'Probability'],
        ['9709', '2024', 'June', '5', '2', '3', 'Discrete Random Variables'],
        ['9709', '2024', 'June', '5', '2', '4', 'Permutations and Combinations'],
        ['9709', '2024', 'June', '5', '2', '5', 'The Normal Distribution'],
        ['9709', '2024', 'June', '5', '2', '6', 'The Normal Distribution'],
        ['9709', '2024', 'June', '5', '2', '7', 'Probability']
    ]
    
    # 9709 June 2024 Variant 13 (P1)
    q_topics_s24_13 = [
        ['9709', '2024', 'June', '1', '3', '1', 'Series'],
        ['9709', '2024', 'June', '1', '3', '2', 'Differentiation'],
        ['9709', '2024', 'June', '1', '3', '3', 'Circular Measure'],
        ['9709', '2024', 'June', '1', '3', '4', 'Trigonometry'],
        ['9709', '2024', 'June', '1', '3', '5', 'Integration'],
        ['9709', '2024', 'June', '1', '3', '6', 'Functions'],
        ['9709', '2024', 'June', '1', '3', '7', 'Differentiation'],
        ['9709', '2024', 'June', '1', '3', '8', 'Coordinate Geometry'],
        ['9709', '2024', 'June', '1', '3', '9', 'Integration'],
        ['9709', '2024', 'June', '1', '3', '10', 'Trigonometry'],
        ['9709', '2024', 'June', '1', '3', '11', 'Coordinate Geometry']
    ]

    # 9709 June 2024 Variant 33 (P3)
    q_topics_s24_33 = [
        ['9709', '2024', 'June', '3', '3', '1', 'Algebra'],
        ['9709', '2024', 'June', '3', '3', '2', 'Complex Numbers'],
        ['9709', '2024', 'June', '3', '3', '3', 'Logarithmic and Exponential Functions'],
        ['9709', '2024', 'June', '3', '3', '4', 'Vectors'],
        ['9709', '2024', 'June', '3', '3', '5', 'Differential Equations'],
        ['9709', '2024', 'June', '3', '3', '6', 'Integration'],
        ['9709', '2024', 'June', '3', '3', '7', 'Trigonometry'],
        ['9709', '2024', 'June', '3', '3', '8', 'Numerical Solutions of Equations'],
        ['9709', '2024', 'June', '3', '3', '9', 'Differentiation'],
        ['9709', '2024', 'June', '3', '3', '10', 'Complex Numbers'],
        ['9709', '2024', 'June', '3', '3', '11', 'Vectors']
    ]

    # 9709 June 2024 Variant 53 (S1)
    q_topics_s24_53 = [
        ['9709', '2024', 'June', '5', '3', '1', 'Representation of Data'],
        ['9709', '2024', 'June', '5', '3', '2', 'Probability'],
        ['9709', '2024', 'June', '5', '3', '3', 'Discrete Random Variables'],
        ['9709', '2024', 'June', '5', '3', '4', 'Permutations and Combinations'],
        ['9709', '2024', 'June', '5', '3', '5', 'The Normal Distribution'],
        ['9709', '2024', 'June', '5', '3', '6', 'The Normal Distribution'],
        ['9709', '2024', 'June', '5', '3', '7', 'Probability']
    ]
    
    # 9709 March 2024 Variant 12 (P1)
    q_topics_m24_12 = [
        ['9709', '2024', 'March', '1', '2', '1', 'Series'],
        ['9709', '2024', 'March', '1', '2', '2', 'Differentiation'],
        ['9709', '2024', 'March', '1', '2', '3', 'Circular Measure'],
        ['9709', '2024', 'March', '1', '2', '4', 'Trigonometry'],
        ['9709', '2024', 'March', '1', '2', '5', 'Integration'],
        ['9709', '2024', 'March', '1', '2', '6', 'Functions'],
        ['9709', '2024', 'March', '1', '2', '7', 'Differentiation'],
        ['9709', '2024', 'March', '1', '2', '8', 'Coordinate Geometry'],
        ['9709', '2024', 'March', '1', '2', '9', 'Integration'],
        ['9709', '2024', 'March', '1', '2', '10', 'Trigonometry'],
        ['9709', '2024', 'March', '1', '2', '11', 'Coordinate Geometry']
    ]

    # 9709 March 2024 Variant 32 (P3)
    q_topics_m24_32 = [
        ['9709', '2024', 'March', '3', '2', '1', 'Algebra'],
        ['9709', '2024', 'March', '3', '2', '2', 'Complex Numbers'],
        ['9709', '2024', 'March', '3', '2', '3', 'Logarithmic and Exponential Functions'],
        ['9709', '2024', 'March', '3', '2', '4', 'Vectors'],
        ['9709', '2024', 'March', '3', '2', '5', 'Differential Equations'],
        ['9709', '2024', 'March', '3', '2', '6', 'Integration'],
        ['9709', '2024', 'March', '3', '2', '7', 'Trigonometry'],
        ['9709', '2024', 'March', '3', '2', '8', 'Numerical Solutions of Equations'],
        ['9709', '2024', 'March', '3', '2', '9', 'Differentiation'],
        ['9709', '2024', 'March', '3', '2', '10', 'Complex Numbers'],
        ['9709', '2024', 'March', '3', '2', '11', 'Vectors']
    ]

    # 9709 March 2024 Variant 52 (S1)
    q_topics_m24_52 = [
        ['9709', '2024', 'March', '5', '2', '1', 'Representation of Data'],
        ['9709', '2024', 'March', '5', '2', '2', 'Probability'],
        ['9709', '2024', 'March', '5', '2', '3', 'Discrete Random Variables'],
        ['9709', '2024', 'March', '5', '2', '4', 'Permutations and Combinations'],
        ['9709', '2024', 'March', '5', '2', '5', 'The Normal Distribution'],
        ['9709', '2024', 'March', '5', '2', '6', 'The Normal Distribution'],
        ['9709', '2024', 'March', '5', '2', '7', 'Probability']
    ]
    
    all_q_topics = q_topics_11 + q_topics_12 + q_topics_13 + q_topics_31 + q_topics_32 + q_topics_23 + q_topics_51 + q_topics_52 + q_topics_53 + \
                   q_topics_s25_11 + q_topics_s25_31 + q_topics_s25_51 + \
                   q_topics_s25_12 + q_topics_s25_32 + q_topics_s25_52 + \
                   q_topics_s25_13 + q_topics_s25_33 + q_topics_s25_53 + \
                   q_topics_m25_12 + q_topics_m25_32 + q_topics_m25_52 + \
                   q_topics_w24_11 + q_topics_w24_31 + q_topics_w24_51 + \
                   q_topics_w24_12 + q_topics_w24_32 + q_topics_w24_52 + \
                   q_topics_w24_13 + q_topics_w24_33 + q_topics_w24_53 + \
                   q_topics_s24_11 + q_topics_s24_31 + q_topics_s24_51 + \
                   q_topics_s24_12 + q_topics_s24_32 + q_topics_s24_52 + \
                   q_topics_s24_13 + q_topics_s24_33 + q_topics_s24_53 + \
                   q_topics_m24_12 + q_topics_m24_32 + q_topics_m24_52
    for qt in all_q_topics:
        append_to_csv('data/question_topics.csv', qt)

if __name__ == "__main__":
    update_topics()
    update_question_topics()
