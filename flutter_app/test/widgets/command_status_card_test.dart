import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import '../../lib/widgets/command_status_card.dart';

void main() {
  testWidgets('CommandStatusCard renders title and subtitle', (WidgetTester tester) async {
    await tester.pumpWidget(
      const MaterialApp(
        home: Scaffold(
          body: CommandStatusCard(
            title: 'MCP Server Online',
            subtitle: 'Netlify Direct Hosting Pipeline active',
          ),
        ),
      ),
    );

    expect(find.text('MCP Server Online'), findsOneWidget);
    expect(find.text('Netlify Direct Hosting Pipeline active'), findsOneWidget);
  });
}
