// https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supply_set = set(supplies)
        graph = dict()
        for recipe in recipes:
            graph[recipe] = [[], 0]
            
        for i, recipe in enumerate(recipes):
            for ing in ingredients[i]:
                if ing not in supplies:
                    try:
                        graph[ing][0].append(recipe)
                        graph[recipe][1] += 1
                    except:
                        graph[ing] = [recipe, 1]
                        graph[recipe][1] += 1
     
        res = []
        queue = []
        for r in graph:
            if graph[r][1] == 0:
                queue.append(r)
        
        while queue:
            cur_r = queue.pop(0)
            res.append(cur_r)
            for next_r in graph[cur_r][0]:
                graph[next_r][1] -= 1
                if graph[next_r][1] == 0:
                    queue.append(next_r)
        
        return res
                        