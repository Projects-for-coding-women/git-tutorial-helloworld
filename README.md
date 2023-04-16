# git-tutorial-helloworld

This repository is used to practice working collaboratively
## Preparation
Clone the repository

```
git clone https://github.com/CodeWomen-Barcelona/git-tutorial-helloworld.git
```

## Exercise 1 

Let us know how you say Hello World in your language

1. Create a file inside `helloworld/` called `my-name.txt` 
2. Inside the file, write how you would say hello in your language! You can also get creative and write anything you want.
3. Push to the develop branch

```
git add helloworld/my-name.txt
git commit -m "added Hello in my language"
git push
```


## Exercise 2


1. Modify the file inside `food/favourite_food.csv` by adding your name and favourite food
2. Create a new branch with your name and push your changes
```
git checkout -b xxx-favourite-food
git add food/favourite_food.csv
git commit -m "added my favourite food"
git push -u origin xxx-favourite-food
```
4. Go to [github](https://github.com/CodeWomen-Barcelona/git-tutorial-helloworld) and open a Pull Request with your changes

5. Ask for someone to approve and 

## Exercise 3

1. Go to [Open Issues](https://github.com/CodeWomen-Barcelona/git-tutorial-helloworld/issues), pick one and assign yourself to it
2. Create a branch and work on it.
3. When you've addressed the issue, open a Pull request and ask someone to approve it
