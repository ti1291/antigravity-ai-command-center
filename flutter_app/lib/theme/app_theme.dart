// Auto-generated from DESIGN.md by custom-design-system skill
import 'package:flutter/material.dart';

class AppDesignTokens {
  static const Color bgPrimary = Color(0xFF0B0F17);
  static const Color bgSurface = Color(0xFF111827);
  static const Color bgElevated = Color(0xFF1F2937);
  static const Color textPrimary = Color(0xFFF9FAFB);
  static const Color textSecondary = Color(0xFF9CA3AF);
  static const Color accentPrimary = Color(0xFF10B981);
  static const Color accentSecondary = Color(0xFF0EA5E9);
  static const Color borderSubtle = Color(0xFF1E293B);

  static ThemeData get darkTheme => ThemeData(
        useMaterial3: true,
        brightness: Brightness.dark,
        scaffoldBackgroundColor: bgPrimary,
        colorScheme: const ColorScheme.dark(
          primary: accentPrimary,
          secondary: accentSecondary,
          surface: bgSurface,
        ),
      );
}
