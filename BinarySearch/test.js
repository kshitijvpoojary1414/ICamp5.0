function getVal( comedyRelease, comedyDuration, dramaRelease, dramaDuration){
  let mapOfComedy = {};
  const len = comedyRelease.length;
  for(let i = 0; i < len; i++){
    mapOfComedy[comedyRelease[i]] = comedyDuration[i]
  }
  console.log(mapOfComedy)
}
let comedyRelease = [1,2,3],
comedyDuration = [1,1,1],
dramaRelease = [1,2,3],
dramaDuration = [10, 5, 1],

getVal(comedyRelease, comedyDuration, dramaRelease, dramaDuration);

