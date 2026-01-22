import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class Welcome extends StatefulWidget {
  final String email;

  const Welcome({super.key, required this.email});

  @override
  State<Welcome> createState() => _WelcomeState();
}

class _WelcomeState extends State<Welcome> {
  Map<String, dynamic>? data;

  @override
  void initState() {
    super.initState();
    fetchUserData();
  }

  void fetchUserData() async {
    var url = Uri.parse("http://127.0.0.1:8000/auth/user/${widget.email}");
    var response = await http.get(url);
    if (response.statusCode == 200) {
      data = jsonDecode(response.body);
      print("User Data: $data");
    } else {
      print("Failed to fetch user data");
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Text("Welcome, ${data!["username"]}", style: TextStyle(fontSize: 24)),
          SizedBox(height: 20),
          data != null
              ? Text("User Info: ${data.toString()}")
              : Text("No user data fetched yet."),
        ],
      ),
    );
  }
}
