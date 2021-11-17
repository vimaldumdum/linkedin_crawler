package main

import (
	"bytes"
	"fmt"
	"log"
	"os/exec"
)

const commandToUse = "python3"

func Shellout(li_at string, url string) (error, string, string) {
	var stdout bytes.Buffer
	var stderr bytes.Buffer
	cmd := exec.Command(commandToUse, "main.py", li_at, url)
	cmd.Stdout = &stdout
	cmd.Stderr = &stderr
	err := cmd.Run()
	return err, stdout.String(), stderr.String()
}

func main() {
	//put li_at value here
	li_at := "li_at here" // li_at here as string
	url := "user_url" // user url here as string
	err, out, errout := Shellout(li_at, url)
	if err != nil {
		log.Printf("error: %v\n", err)
		//error handling here
		fmt.Println("--- stderr ---")
		fmt.Println(errout)
	} else {
		fmt.Println("--- stdout ---")
		fmt.Println(out)
	}
}
