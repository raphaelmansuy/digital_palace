# How to publish a Rust cli tool to homebrew

Here is a step-by-step guide on how to publish your hiramu-cli tool to Homebrew:

1. Create a GitHub release for your tool
- Tag your latest commit with a version number, e.g. v0.1.0
```bash
git tag -a v0.1.0 -m "Release v0.1.0"
git push origin v0.1.0  
```
- On GitHub, go to your hiramu-cli repo, click Releases, and create a new release using the tag you just pushed
- Attach any binaries or assets to the release

2. Create a new GitHub repository called homebrew-tap 
- This will host your custom Homebrew formula
- Initialize it with a README file

3. Create the Homebrew formula
- In your homebrew-tap repo, create a new file called hiramu-cli.rb with this template:
```ruby
class HiramuCli < Formula
  desc "A CLI tool for interacting with LLMs"
  homepage "https://github.com/yourusername/hiramu-cli"
  url "https://github.com/yourusername/hiramu-cli/archive/refs/tags/v0.1.0.tar.gz"
  sha256 "REPLACE_WITH_SHA256_OF_TAR_FILE"
  license "MIT"

  depends_on "rust" => :build

  def install
    system "cargo", "install", *std_cargo_args
  end
end
```
- Replace REPLACE_WITH_SHA256_OF_TAR_FILE with the SHA256 hash of the .tar.gz file from your GitHub release
- Modify the other metadata like desc, homepage, license as needed

4. Test the formula 
- Tap your repository and install the formula locally:
```bash 
brew tap yourusername/tap
brew install hiramu-cli
```
- Verify that hiramu-cli installs and runs correctly

5. Create a pull request to the homebrew-core repo (optional)
- Fork the Homebrew/homebrew-core repo on GitHub  
- Create a new branch, copy your hiramu-cli.rb formula into the Formula directory
- Open a pull request to merge your branch into master
- A Homebrew maintainer will review your PR and provide feedback

6. Share your tap 
- Users can now install your tool directly from your tap:
```bash
brew tap yourusername/tap
brew install hiramu-cli
```
- Add installation instructions to your hiramu-cli README, linking to your tap

