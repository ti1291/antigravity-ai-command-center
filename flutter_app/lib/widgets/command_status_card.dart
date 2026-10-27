import 'package:flutter/material.dart';
import '../theme/app_theme.dart';

class CommandStatusCard extends StatelessWidget {
  final String title;
  final String subtitle;

  const CommandStatusCard({
    super.key,
    required this.title,
    required this.subtitle,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: AppDesignTokens.bgSurface,
        borderRadius: BorderRadius.circular(10),
        border: Border.all(color: AppDesignTokens.borderSubtle),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisSize: MainAxisSize.min,
        children: [
          Text(
            title,
            style: const TextStyle(
              color: AppDesignTokens.textPrimary,
              fontSize: 16,
              fontWeight: FontWeight.w600,
            ),
          ),
          const SizedBox(height: 6),
          Text(
            subtitle,
            style: const TextStyle(
              color: AppDesignTokens.textSecondary,
              fontSize: 13,
            ),
          ),
        ],
      ),
    );
  }
}
