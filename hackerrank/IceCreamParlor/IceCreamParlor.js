// Brute force Solution
// function whatFlavors(cost, money) {
//     for (let i = 0; i < cost.length; i++) {
//         for (let j = 0; j < cost.length; j++) {
//             if (cost[i] + cost[j] === money && i != j) {
//                 if (i < j) { console.log(i + 1, j + 1); return}
//                 else { console.log(j + 1, i + 1); return }
//             }
//         }
//     }

// }
// Solution using a Hash Table
function whatFlavors(costs, money) {
    const compliments = {} // key: val = const: index
    
    // loop through costs
    for (let i = 0; i < costs.length; i++) {
        const cost = costs[i]
        // skip any cost that is larger or equal to money
        if (cost >= money) continue;
        // check if cost is in compliments, 
        const compliment = money - cost
        if (compliments[cost]){
            const costIndex = i + 1
            const complimentIndex = compliments[cost]
            const min = Math.min(costIndex, complimentIndex)
            const max = Math.max(costIndex, complimentIndex)
            console.log(`${min} ${max} `)
            return
        }
        compliments[compliment] = i + 1
    }
}


const cost = [1, 2, 3, 5, 6]
const money = 5

console.log(whatFlavors(cost, money))