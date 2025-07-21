#!/usr/bin/env python3
"""
Template Test Script - Verify BotCity template functionality
Tests template loading and basic detection capabilities
"""

import time
from pathlib import Path

try:
    from botcity.core import DesktopBot
    print("✅ BotCity imports successful")
except ImportError as e:
    print(f"❌ BotCity import failed: {e}")
    print("💡 Run: pip install botcity-framework-core botcity-framework-base")
    exit(1)

class TemplateTestBot(DesktopBot):
    def __init__(self):
        super().__init__()
        
        # Set up templates directory
        self.templates_dir = Path(__file__).parent / "templates"
        
        if not self.templates_dir.exists():
            print(f"❌ Templates directory not found: {self.templates_dir}")
            return
        
        # Load templates
        self.load_templates()
    
    def load_templates(self):
        """Load all available templates"""
        templates = [
            ("textedit_window", "textedit_window.png"),
            ("save_dialog", "save_dialog.png"),
            ("save_button", "save_button.png"),
            ("use_both_extensions", "use_both_extensions.png"),
            ("use_both_extensions_button", "use_both_extensions_button.png")
        ]
        
        loaded_templates = []
        missing_templates = []
        
        for template_name, template_file in templates:
            template_path = self.templates_dir / template_file
            if template_path.exists():
                self.add_image(template_name, str(template_path))
                loaded_templates.append(template_name)
                print(f"✅ Loaded template: {template_name}")
            else:
                missing_templates.append(template_file)
                print(f"❌ Missing template: {template_file}")
        
        print(f"\n📊 Template Summary:")
        print(f"   ✅ Loaded: {len(loaded_templates)}")
        print(f"   ❌ Missing: {len(missing_templates)}")
        
        if missing_templates:
            print(f"\n💡 Create these template images:")
            for template in missing_templates:
                print(f"   - templates/{template}")
    
    def test_screenshot(self):
        """Test screenshot functionality"""
        try:
            print("\n📸 Testing screenshot capability...")
            screenshot_path = self.get_screenshot()
            print(f"✅ Screenshot taken: {screenshot_path}")
            return True
        except Exception as e:
            print(f"❌ Screenshot failed: {e}")
            return False
    
    def test_template_detection(self):
        """Test template detection on current screen"""
        print("\n🔍 Testing template detection on current screen...")
        print("   (Note: Templates may not be found if apps aren't open)")
        
        templates_to_test = ["textedit_window", "save_dialog", "save_button", "use_both_extensions", "use_both_extensions_button"]
        
        for template in templates_to_test:
            try:
                print(f"   Looking for {template}...")
                if self.find(template, matching=0.7, waiting_time=1000):
                    print(f"   ✅ Found: {template}")
                else:
                    print(f"   ❌ Not found: {template} (expected if app not open)")
            except Exception as e:
                print(f"   ❌ Error testing {template}: {e}")
    
    def test_ocr(self):
        """Test OCR functionality"""
        print("\n📝 Testing OCR functionality...")
        
        # Test common text that might be on screen
        test_texts = ["File", "Edit", "View", "Window"]
        
        found_texts = []
        for text in test_texts:
            try:
                if self.find_text(text, matching=0.8, waiting_time=1000):
                    found_texts.append(text)
                    print(f"   ✅ Found text: '{text}'")
            except Exception as e:
                print(f"   ❌ Error looking for '{text}': {e}")
        
        if found_texts:
            print(f"   📊 OCR working - found {len(found_texts)} text elements")
        else:
            print("   ⚠️  No text found (OCR may need adjustment or no text visible)")

def main():
    """Main test function"""
    print("🧪 BotCity Template Test")
    print("=" * 40)
    
    # Create test bot
    try:
        bot = TemplateTestBot()
        print("✅ Test bot created successfully")
    except Exception as e:
        print(f"❌ Failed to create test bot: {e}")
        return
    
    # Run tests
    print("\n🏃 Running Tests...")
    
    # Test 1: Screenshot
    bot.test_screenshot()
    
    # Test 2: Template detection
    bot.test_template_detection()
    
    # Test 3: OCR
    bot.test_ocr()
    
    # Final summary
    print("\n" + "=" * 40)
    print("🎯 Test Complete!")
    print("\n💡 Next Steps:")
    print("   1. Ensure all templates exist in templates/ directory")
    print("   2. Run: python enhanced_bot.py")
    print("   3. Compare with: python desktop_bot.py")
    
    print("\n🎤 Interview Points:")
    print("   ✅ Template-based UI detection")
    print("   ✅ OCR text recognition")  
    print("   ✅ Screenshot evidence collection")
    print("   ✅ Robust error handling")

if __name__ == "__main__":
    main() 