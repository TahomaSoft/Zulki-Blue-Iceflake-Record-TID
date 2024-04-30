package main

import (
	"fmt"
	"github.com/bluesky-social/indigo/atproto/syntax"
)

func main() {
	str := "22jbdcehcncry"
	fmt.Println(str)
	if _, err := syntax.ParseTID(str); err != nil {
		fmt.Println("NOT a valid TID")
	} else {
		fmt.Println("IS a valid TID")
	}
	if _, err := syntax.ParseRecordKey(str); err != nil {
		fmt.Println("NOT a valid record key")
	} else {
		fmt.Println("IS a valid record key")
	}
}
