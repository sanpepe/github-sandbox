const core = require("@actions/core");
const github = require("@actions/github");

try {
    const name = core.getInput("who-to-say-hello");
    console.log(`Hello World ${name}`);

    const time = new Date();
    core.setOutput("time", time.toTimeString());
    console.log(JSON.stringify(github, null, '  '));

} catch(error) {
    // You can call this function to make action and workflow fail
    core.setFailed(error.message)
}
