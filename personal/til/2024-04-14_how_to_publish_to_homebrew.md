# 2024-04-14: Publishing a Rust CLI Tool to Homebrew

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> Learn how to create a Homebrew formula for your Rust CLI tool, enabling easy installation for macOS users through the `brew install` command with custom taps and proper dependency management.

## The Pain Point

Distributing CLI tools to macOS users requires:

- Manual download and installation instructions
- Users having to manage dependencies themselves
- Complex PATH configuration for binaries
- No easy update mechanism for users
- Inconsistent installation experience across platforms

Homebrew solves this by providing a standardized package management system that handles dependencies, installation, and updates automatically.

## Step-by-Step Guide

### 1. Create a GitHub Release

```bash
# Tag your latest commit with a semantic version
git tag -a v0.1.0 -m "Release v0.1.0"
git push origin v0.1.0

# Verify the tag was created
git tag -l
```

Then on GitHub:

- Go to your repository → Releases → Create new release
- Select the tag you just created
- Add release notes describing features and changes
- Attach any pre-built binaries (optional but recommended)

### 2. Set Up Homebrew Tap Repository

```bash
# Create a new repository on GitHub named 'homebrew-tap'
# Clone it locally
git clone https://github.com/yourusername/homebrew-tap.git
cd homebrew-tap

# Create the Formula directory
mkdir Formula
```

### 3. Create the Homebrew Formula

Create `Formula/hiramu-cli.rb`:

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

  test do
    # Add a simple test to verify installation
    system "#{bin}/hiramu-cli", "--version"
  end
end
```

### 4. Calculate SHA256 Hash

```bash
# Download the release tarball
curl -L -o hiramu-cli-v0.1.0.tar.gz https://github.com/yourusername/hiramu-cli/archive/refs/tags/v0.1.0.tar.gz

# Calculate SHA256 hash
shasum -a 256 hiramu-cli-v0.1.0.tar.gz

# Copy the hash and replace REPLACE_WITH_SHA256_OF_TAR_FILE in your formula
```

### 5. Test the Formula Locally

```bash
# Tap your repository locally
brew tap yourusername/tap

# Install from your tap
brew install hiramu-cli

# Test the installation
hiramu-cli --version
hiramu-cli --help

# Uninstall for testing
brew uninstall hiramu-cli
```

### 6. Commit and Push Your Formula

```bash
cd homebrew-tap
git add Formula/hiramu-cli.rb
git commit -m "Add hiramu-cli formula v0.1.0"
git push origin main
```

### 7. Advanced Formula Features

```ruby
class HiramuCli < Formula
  desc "A CLI tool for interacting with LLMs"
  homepage "https://github.com/yourusername/hiramu-cli"
  url "https://github.com/yourusername/hiramu-cli/archive/refs/tags/v0.1.0.tar.gz"
  sha256 "abc123..."
  license "MIT"
  head "https://github.com/yourusername/hiramu-cli.git"

  depends_on "rust" => :build
  depends_on "openssl@3"

  def install
    system "cargo", "install", *std_cargo_args
    
    # Install shell completions
    bash_completion.install "completions/hiramu-cli.bash"
    zsh_completion.install "completions/_hiramu-cli"
    fish_completion.install "completions/hiramu-cli.fish"
    
    # Install man page
    man1.install "docs/hiramu-cli.1"
  end

  test do
    system "#{bin}/hiramu-cli", "--version"
    assert_match "hiramu-cli", shell_output("#{bin}/hiramu-cli --help")
  end
end
```

### 8. Update for New Releases

```bash
# For each new release, update the formula
# 1. Update the version in the URL
# 2. Calculate new SHA256 hash
# 3. Commit and push changes

# Example for v0.2.0
git tag -a v0.2.0 -m "Release v0.2.0"
git push origin v0.2.0

# Update formula with new URL and SHA256
# Commit changes
git commit -am "Update hiramu-cli to v0.2.0"
git push origin main
```

## Troubleshooting

### SHA256 Mismatch Errors

- Ensure you're downloading the exact same tarball that GitHub generates
- Use `curl -L` to follow redirects when downloading
- Double-check the URL format in your formula

### Build Failures

```bash
# Debug build issues
brew install --verbose --debug hiramu-cli

# Check build logs
brew gist-logs hiramu-cli

# Test build locally
brew install --build-from-source hiramu-cli
```

### Dependency Issues

- Ensure all required dependencies are listed in `depends_on`
- Use `depends_on "dependency" => :build` for build-time dependencies
- Check that dependencies are available in Homebrew core

### Formula Audit Failures

```bash
# Run Homebrew audit to check formula quality
brew audit --strict hiramu-cli

# Fix common issues:
# - Add proper test block
# - Ensure proper licensing
# - Check formula naming conventions
```

## Related Resources

- [Homebrew Formula Cookbook](https://docs.brew.sh/Formula-Cookbook) - Complete guide to writing formulas
- [Homebrew Acceptable Formulae](https://docs.brew.sh/Acceptable-Formulae) - Guidelines for submitting to homebrew-core
- [Rust Cargo Integration](https://docs.brew.sh/FAQ#why-does-homebrew-say-a-formula-is-missing) - Best practices for Rust projects
- [Creating Taps](https://docs.brew.sh/How-to-Create-and-Maintain-a-Tap) - Managing your own Homebrew tap
- [Homebrew Cask](https://github.com/Homebrew/homebrew-cask) - For distributing GUI applications

