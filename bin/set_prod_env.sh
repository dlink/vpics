# deactivate virtual_env if necessary
if [[ -n "${VIRTUAL_ENV:-}" ]] && declare -F deactivate >/dev/null; then
    deactivate
fi

# production environment
export vp=/apps/vpics
cd "$vp" || return 1
source "$vp/.venv/bin/activate"
source "$vp/bin/aliases"
export PYTHONPATH="$vp/lib"
export VCONF=/data/media/sebastianlinkmusic/vpics.yaml
export VPICS_THUMBNAIL_DIR=300px
export VPICS_PAGE_COLUMNS=illustrator2:1
export PATH="$PATH:$vp/bin:$vp/lib"

echo VCONF="$VCONF"
echo PYTHONPATH="$PYTHONPATH"
