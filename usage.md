
### USAGE.md

```markdown
# Usage Guide for Pomodoro Timer

This guide provides detailed instructions on how to use the Pomodoro Timer and Stopwatch functions included in the package.

## Pomodoro Timer

The Pomodoro Timer helps you manage your work by breaking it into intervals of focused work followed by short breaks.

### Starting the Pomodoro Timer

1. Run the following command in your terminal:

    ```sh
    Pomodoro_Timer
    ```

2. You will be prompted to enter the work duration in minutes. For example:

    ```sh
    Enter work duration in minutes: 25
    ```

3. The timer will start and display the countdown:

    ```
    Start working! Pomodoro timer started.
    ```

4. When the work interval ends, you will hear an audible alert. The timer will then prompt you for a break:

    ```
    Time for a short break!
    ```

5. After four work intervals, you will have a longer break.

### Stopping the Pomodoro Timer

- Press the `spacebar` at any time to stop the timer and exit the program.

## Stopwatch

The Stopwatch function allows you to measure elapsed time.

### Starting the Stopwatch

1. Run the following command in your terminal:

    ```sh
    Pomodoro_Timer stopwatch
    ```

2. The stopwatch will start and display the elapsed time:

    ```
    Stopwatch started. Press spacebar to stop.
    ```

### Stopping the Stopwatch

- Press the `spacebar` to stop the stopwatch and display the final elapsed time:

    ```
    Stopwatch stopped.
    ```

## Customizing Intervals

By default, the work interval is set to 25 minutes, short breaks to 5 minutes, and long breaks to 15 minutes. Currently, these settings are not customizable via the command line but can be modified in the script.

## Example

Below is an example of using the Pomodoro Timer:

```sh
$ Pomodoro_Timer
Enter work duration in minutes: 25
Start working! Pomodoro timer started.
00:24:59
...
00:00:01
Time for a short break!
