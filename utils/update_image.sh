#!/bin/bash

mediapath=/home/insalan/ES-DE/downloaded_media
#rompath=/media/insalan/BorneInsalan/ROMs
rompath=/home/insalan/ROMs
gamelistpath=/home/insalan/ES-DE/gamelists
collecpath=/home/insalan/ES-DE/collections
systemscfg=./systems.xml

# Does a list contain an element?
contains_element() {
	local e match="$1"
	shift
	for e; do 
		[[ "$e" == "$match" ]] && return 0
	done
	return 1
}

# Look for ROM suitable extensions
build_ext_array() {
	all_ext=$(xmllint --xpath '/systemList/system/extension/text()' ${systemscfg} 2>/dev/null)
	ext_array="" 
	for i in ${all_ext}; do
		! contains_element ${i} ${ext_array} && ext_array="$i $ext_array" 
	done
	extensions="("$(echo ${ext_array}|sed "s/ /|/g")")"
}

# First, let's do a match with ROM filenames
# We'll parse only roms from matching extensions
parse_filenames() {
	fn=$(date +"%s")
	tmpfile=/tmp/collec_${fn}
	depth=1
	[[ -z $systempath ]] && depth=2
	find ${rompath}/${systempath} -maxdepth ${depth} -type f | egrep -i "${rompath}.*.*${extensions}" > ${tmpfile}
	systemslist=$(find ${gamelistpath}/${systempath} -maxdepth ${depth} -type d)
	while IFS= read -r game; do 
		base=$(basename "$game") # Get game name
		base_wo_ext="${base%.*}"
		parentdir="$(dirname "$game")" 
		curr_system=$(basename "$parentdir") # Get system name
		# to avoid matching "mega" search term with "megadrive" in the path
		[[ -z $base ]] && continue
		# remove [...] in the filename to avoid regex errors
		cleangame=$(echo $game | sed "s:\[.*::")

		##Open XML from gamelist
		gamelist="${gamelistpath}/${curr_system}/gamelist.xml"
		
		xmlstarlet ed -L -d "//gameList/game/image" ${gamelist} 2> /dev/null #On suppr d'abord tout le bordel avec images

		cover=$(ls "${mediapath}/${curr_system}/covers/${base_wo_ext}".* 2> /dev/null)
		cover_test=$(ls "${mediapath}/${curr_system}/covers/${base_wo_ext}".* 2> /dev/null | wc -l) #flemme propre
		if [ "$cover_test" != "0" ] 
		then
			sed -i "s:${base}</path>:${base}</path>\n<image>${cover}</image>:g" ${gamelist}
		fi

	done < ${tmpfile}
	[[ -f $tmpfile ]] && rm ${tmpfile}

	
}

# Main loop
build_ext_array
parse_filenames
#nb_games=$(cat ${filecollection} 2>/dev/null | wc -l)
#echo "Added ${new_found} games to the custom collection '$(basename ${filecollection})' (total:${nb_games})"
