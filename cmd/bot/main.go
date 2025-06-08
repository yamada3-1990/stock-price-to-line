package main

import (
	"fmt"
	"os/exec"
)

func main() {
	cmd := exec.Command("python", "scripts/test.py")

	output, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Println("command exec Error:", err)
	}
	fmt.Println("Output:\n", string(output))
}
