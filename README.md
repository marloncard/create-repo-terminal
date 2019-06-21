# CREATE GIT REPO
A simple python script to create a github repository from the comfort of your terminal. With proper setup this can be called from anywhere. Returns the ssh link to your new repo.

## CONTENTS
1. [Requirements](#requirements)
2. [Token](#github-token)
3. [Local Setup](#local-setup)

## REQUIREMENTS
* Github Personal Access Token
* Python 3.x
* Python's `requests` library installed system wide
* This might require some modification to the token path to work in windows

## Github Token
Create a GitHub Personal Access Token [here](https://github.com/settings/tokens)

## Local Setup
1. Create a `.credentials` folder in your home directory
2. Create a `GITHUB.txt` file inside that folder and add your token.
3. Username is hard coded on line 38, update to yours.
4. Copy file to a wherever you keep scripts, ie: `cp createrepo.py ~/bin/` and rename if you want `mv createrepo.py createrepo`
5. Make file executable with `chmod +x createrepo`
6. Make sure to add this directory to your path by adding the following to your `.bashrc` or `.bash_profile`:

 ```
 export PATH=~/bin:$PATH
 ```

7. Test that it's working by running `createrepo` from outside the `~/bin` directory