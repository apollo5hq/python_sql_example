# Python SQL Example

This repo contains a simple Python application using MySQL to demonstrate PR reviews from [SeniorDev](https://seniordev.ai).

## About

This code implements a basic CRUD app with Python, MySQL, and FastAPI. It has APIs to:

- Get all items
- Add a new item

The goals are:

1. Provide a sample Python codebase that uses a database
2. Demonstrate PR reviews and automated feedback from SeniorDev
3. Showcase best practices for Python, SQL, code quality

SeniorDev analyzes every PR opened against this repo. It provides automated reviews about:

- Code quality
- Security issues
- Performance problems
- Bug risks
- Style violations
- Documentation needs

The feedback from SeniorDev helps improve the overall code quality and developer skills.

## Usage

- Clone the repo
- Create a virtualenv and install requirements
- Configure MySQL connection settings
- Run the application:

```
uvicorn app:app --reload
```

- API endpoints:

  - GET /items - Get all items
  - POST /items - Create new item
  
- Open PRs with some sample changes to see SeniorDev reviews in action!

## Contributing

Pull requests are welcome! Open a PR to suggest improvements or fix bugs and watch as SeniorDev provides feedback. This repo is intended to demonstrate collaborative development workflows.

Want a review on your own codebase? Have a review in less than 5 minutes at [SeniorDev](https://app.seniordev.ai). 

## License

This project is licensed under the MIT license. See [LICENSE](LICENSE) for more details.
