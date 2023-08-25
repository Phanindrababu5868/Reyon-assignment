def steadyGene(gene):
    n = len(gene)
    target_count = n // 4

    excess = {
        'A': max(0, gene.count('A') - target_count),
        'C': max(0, gene.count('C') - target_count),
        'G': max(0, gene.count('G') - target_count),
        'T': max(0, gene.count('T') - target_count)
    }

    if all(count == 0 for count in excess.values()):
        return 0

    min_length = n
    left = 0

    for right in range(n):
        excess[gene[right]] -= 1

        while all(count <= 0 for count in excess.values()):
            min_length = min(min_length, right - left + 1)
            excess[gene[left]] += 1
            left += 1

    return min_length

n = int(input())
gene = input().strip()

# Calculate and print the result
result = steadyGene(gene)
print(result)
